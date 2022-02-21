from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from kubernetes import client, config
from django.utils.html import strip_tags
# Create your views here.

@login_required
def rules_view(request):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    confmaps = v1.read_namespaced_config_map("ebpf-policy", "default")
    if (request.method == "POST"):
        rules = request.POST.get('rules')
        rules = strip_tags(rules)
        confmaps.data["example.rules"] = rules
        newconfmaps = v1.replace_namespaced_config_map(name="ebpf-policy",namespace="default", body=confmaps)
        rules = newconfmaps.data["example.rules"]

        return JsonResponse({"rules": rules})

    # Configs can be set in Configuration class directly or using helper utility

    # confmaps = v1.read_namespaced_config_map("ebpf-policy", "default")
    rules = confmaps.data["example.rules"]
    return render(request, 'rules.html', {"rules": rules})