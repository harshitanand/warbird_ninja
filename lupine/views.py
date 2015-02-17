from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from warbird.settings import Github_client_id, Github_client_secret
import requests as req
from uritemplate import expand
from github import Github, GithubException
import json

# Create your views here.
@login_required
def home(request):
    return render(request, 'Index.html')

@login_required
def callback(request):
    url = expand("https://github.com/login/oauth/access_token{?client_id,client_secret,code}",
                 client_id = Github_client_id, client_secret = Github_client_secret, code = request.GET["code"])
    r = req.post(url, headers={"Accept": "application/json"}).json()
    request.session["github_token"] = r["access_token"]
    if r["scope"] == "":
        request.session["github_scopes"] = []
    else:
        request.session["github_scopes"] = r["scope"].split(",")
    return redirect("lupine.views.index")

def index(request):
    g = buildPyGithub(request)
    if g is None:
        return render(request,"Index.html",{"github_authorize_url": "https://github.com/login/oauth/authorize?client_id=f14052faddcf7e3fe42d",})
    else:
        try:
            return render(request,"repolist.html",{"github_authorize_url": "https://github.com/login/oauth/authorize?client_id=f14052faddcf7e3fe42d&scope=repo,user:email,read:repo_hook","repos": g.get_user().get_repos(),"github_scopes": request.session["github_scopes"],})
        except GithubException:
            return render(request,"Index.html",{"github_authorize_url": "https://github.com/login/oauth/authorize?client_id=f14052faddcf7e3fe42d",})

def buildPyGithub(request):
    token = request.session.get("github_token")
    if token is None:
        return None
    else:
        print token
        return Github(login_or_token=token, client_id=Github_client_id, client_secret=Github_client_secret)

def clean(request):
    request.session.clear()
    return redirect(index(request))

def hooks(request):
    if request.method == 'POST':
        reponame = request.POST['repo_name']
        g = buildPyGithub(request)
        owner = g.get_user()
        repo = reponame
        url = expand("https://api.github.com/repos/%s/%s/hooks{?name,config,events}" % (owner,repo),
                    name = "web", config = {"url": "http://example.com/webhook","content_type": "json"}, events = ["push","pull_request","watch"] )
        res = req.post(url, headers={"Accept": "application/json"}).json()
        print reponame, owner
        return render(request, "payload.html", {"payload" : res})