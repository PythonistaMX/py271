import json
import os

notebooks = [
    "12_iam_oidc_y_autenticacion_sin_llaves.ipynb",
    "13_build_contenedores_en_actions.ipynb",
    "14_terraform_fundamentos_y_estado_remoto.ipynb",
    "15_terraform_para_artifact_registry_y_cloud_functions.ipynb",
    "16_terraform_para_compute_engine_y_red.ipynb",
    "17_pipelines_infra_plan_apply.ipynb",
    "18_despliegue_seguro_en_linux.ipynb",
    "19_observabilidad_smoke_tests_y_rollback.ipynb",
    "20_proyecto_final_end_to_end.ipynb"
]

beginner_keywords = [
    'Introduccion desde cero', 
    'Puente rapido', 
    'Recordatorio para principiantes', 
    'modelo operativo de Terraform'
]

results = []

for nb_path in notebooks:
    if not os.path.exists(nb_path):
        continue
    
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        results.append({"Notebook": nb_path, "Error": str(e)})
        continue

    cells = data.get('cells', [])
    
    title = "N/A"
    has_objetivos = False
    beginner_mentions = []

    for cell in cells:
        source_list = cell.get('source', [])
        source_text = "".join(source_list)
        
        # Title search
        if title == "N/A" and cell['cell_type'] == 'markdown':
            for line in source_list:
                if line.strip().startswith('# '):
                    title = line.strip('# \n')
                    break
        
        # Objetivos search
        if '## Objetivos' in source_text:
            has_objetivos = True
        
        # Beginner keywords search
        for kw in beginner_keywords:
            if kw.lower() in source_text.lower():
                if kw not in beginner_mentions:
                    beginner_mentions.append(kw)

    results.append({
        "Notebook": nb_path,
        "Título": title,
        "Objetivos": "Sí" if has_objetivos else "No",
        "Menciones Beginner": ", ".join(beginner_mentions) if beginner_mentions else "Ninguna"
    })

# Print compact table
header = f"{'Notebook':<45} | {'Título':<50} | {'Obj':<3} | {'Menciones'}"
print(header)
print("-" * len(header))
for res in results:
    nb = res["Notebook"]
    title = res["Título"][:50]
    obj = res["Objetivos"]
    menciones = res["Menciones Beginner"]
    print(f"{nb:<45} | {title:<50} | {obj:<3} | {menciones}")

