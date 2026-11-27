# Entornos alternativos para práctica

Repos y labs similares al stack de py271, agrupados por tema.

---

## Stack GCP + GitHub Actions (Google oficial)

**[google-github-actions/example-workflows](https://github.com/google-github-actions/example-workflows)**
Colección oficial de workflows para deploy a Cloud Run, build con Docker/Buildpacks y Cloud Deploy. Equivalente de referencia para los NB12 y NB20 del curso.

**[GoogleCloudPlatform/terraform-google-three-tier-web-app](https://github.com/GoogleCloudPlatform/terraform-google-three-tier-web-app)**
App de tres capas con Cloud Run + Cloud SQL en Terraform. Cubre exactamente lo que el curso construye en NB14-15. Tiene módulos separados para [Cloud Run](https://github.com/GoogleCloudPlatform/terraform-google-cloud-run) y [Cloud SQL](https://github.com/terraform-google-modules/terraform-google-sql-db).

**[mchmarny/oidc-for-gcp-using-terraform](https://github.com/mchmarny/oidc-for-gcp-using-terraform)**
Reproducible: Workload Identity Federation + OIDC con GCP desde Terraform. Paralelo directo al NB16 del curso.

---

## DevSecOps / Cadena de suministro

**[raph-rcn/devsecops-juice-shop](https://github.com/raph-rcn/devsecops-juice-shop)**
Lab end-to-end con OWASP Juice Shop: SBOM con Syft (CycloneDX/SPDX), firma con Cosign (keyless OIDC), SLSA provenance. Cubre el mismo terreno que NB10-11.

**[vamshiarkala/devsecops-lab](https://github.com/vamshiarkala/devsecops-lab)**
Lab minimalista: Docker + Trivy + GitHub Actions. Útil como punto de entrada antes del material de NB11.

**[Supply Chain Security Labs — DevSecOps Guides](https://blog.devsecopsguides.com/p/supply-chain-security-labs)**
Serie de labs: Sigstore, pipelines de firma CI/CD, AWS Signer, provenance (SLSA/in-toto), verificación en deploy y admission control.

---

## Plantilla Python + Cloud Run

**[markdouthwaite/google-cloud-run-python-job](https://github.com/markdouthwaite/google-cloud-run-python-job)**
Template listo para producción: Cloud Run Job en Python con pipeline CI/CD en Actions. Más simple que el app del curso, útil como sandbox limpio.

---

## Recomendación

Para práctica sobre el tramo de mayor peso del curso (NB16 + NB17 + NB20), el par
`mchmarny/oidc-for-gcp-using-terraform` + `google-github-actions/example-workflows`
ofrece exactamente ese entorno replicable como práctica complementaria al material de este curso.
