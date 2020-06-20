"""
@author Willow Maui García Moreno
Prueba de extracción de las issues de un repositorio
"""
import gitlab
import os

# Obtención del Token o login
HOST='http://gitlab.com/'
TOKEN_PATH='..'+os.path.sep+'lib'+os.path.sep+'Token.txt'
TOKEN= open(TOKEN_PATH).read()
gl = gitlab.Gitlab(HOST, private_token=TOKEN)
#project_id = 8860457
#project = gl.projects.get(project_id)
# Repositorio de ejemplo https://gitlab.com/foundrynet/dnd5e
project_url='foundrynet/dnd5e'
project= gl.projects.get(project_url)

#Doc https://docs.gitlab.com/ce/api/issues.html
#issues=project.issues.list(all=True)
issues=project.issues.list()

# Doc https://docs.gitlab.com/ee/api/labels.html
labels = project.labels.list(all=True)

i=0
for label in labels:
    i+=1
    print(i," Label id:",label.id," Name ", label.name)
for issue in issues:
    print("issue id:",issue.iid," Name ", issue.title)
    if (issue.description!=''):
        print("Description ",issue.description)