## Repository-specific guidance for AI code assistants

This repository contains short lab exercises that demonstrate Tekton-based CI/CD pipelines.
Keep instructions concise and focused on the files under `labs/01_base_pipeline`.

- Primary files of interest:
  - `labs/01_base_pipeline/tasks.yaml` — defines a Tekton `Task` (example: `hello-world` using `alpine:3`).
  - `labs/01_base_pipeline/pipeline.yaml` — defines a Tekton `Pipeline` (contains placeholder `name: <place-name-here>`).
  - `labs/01_base_pipeline/README.md` — short lab description; treat the lab folder as the unit of work.

- Big picture (discoverable):
  - This lab shows how to write Tekton CRs: `Task` objects implement steps (container, command, args) and `Pipeline` objects sequence tasks.
  - Tasks are standalone CRs applied to the cluster; the `Pipeline` references tasks by name. Check `apiVersion: tekton.dev/v1beta1` in the YAMLs.

- Concrete, actionable patterns to follow:
  - Preserve the Tekton YAML structure: `apiVersion`, `kind`, `metadata.name`, and `spec.steps` for `Task` objects.
  - When editing `pipeline.yaml`, replace placeholders like `name: <place-name-here>` with a valid resource name before applying.
  - Keep tasks small and self-contained (the example task runs `alpine:3` and echoes text).

- Running and debugging (what works here):
  - Common workflow to apply and test these manifests (assuming Tekton & Kubernetes are installed):
    - `kubectl apply -f labs/01_base_pipeline/tasks.yaml`
    - `kubectl apply -f labs/01_base_pipeline/pipeline.yaml` (after replacing the placeholder name)
    - Optionally use the Tekton CLI: `tkn pipeline start <pipeline-name>` and `tkn pipelinerun logs -f <pipelinerun-name>`
  - Common failure modes to surface in suggestions: wrong `apiVersion`, missing Tekton installation on cluster, RBAC/service account errors, or using image names that cannot be pulled.

- Examples and snippets to reference in suggestions:
  - From `tasks.yaml`: a step uses `image: alpine:3` with `command: [/bin/echo]` and `args: ["Hello, World!"]` — mirror this pattern for simple, single-step tasks.
  - From `pipeline.yaml`: pipelines list `tasks:` — ensure the task names match the `metadata.name` in `Task` resources.

- Conventions & repo-specific notes:
  - This repository contains labs; changes should generally be made inside the relevant `labs/*` folder.
  - No automated tests or CI configs are present in this folder — keep edits minimal and self-verifying (apply to a Tekton cluster and inspect logs).

- When editing or creating new Tekton resources:
  - Validate YAML for proper indentation and Tekton schema (assist by pointing to `apiVersion` used in examples).
  - Recommend including clear `metadata.name`, and avoid leaving placeholders.

If anything here is unclear or you'd like more coverage (e.g., adding examples for `tkn` usage or troubleshooting RBAC errors), tell me which area to expand and I will iterate.
