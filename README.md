<!--
 Copyright 2022 Indoc Research
 
 Licensed under the EUPL, Version 1.2 or – as soon they
 will be approved by the European Commission - subsequent
 versions of the EUPL (the "Licence");
 You may not use this work except in compliance with the
 Licence.
 You may obtain a copy of the Licence at:
 
 https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
 
 Unless required by applicable law or agreed to in
 writing, software distributed under the Licence is
 distributed on an "AS IS" basis,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied.
 See the Licence for the specific language governing
 permissions and limitations under the Licence.
 
-->

# common

Importable Pip package that generates entity ID and connects with Vault (secret engine) to retrieve credentials.

## Import package
Pip install command from GitLab:
```
pip install common --index-url https://__token__:<GITLAB_PAT>@git.indocresearch.org/api/v4/projects/158/packages/pypi/simple
```

Pip install command from `.whl` file:
```
pip install common-<VERSION>-py3-none-any.whl
```

In `requirements.txt`:
```
--index-url https://__token__:<GITLAB_PAT>@git.indocresearch.org/api/v4/projects/158/packages/pypi/simple
common
```

`<GITLAB_PAT>` is a GitLab personal access token with the `read_api` scope.

## Update package
Refer to documentation: https://docs.gitlab.com/ee/user/packages/pypi_repository/#publish-a-pypi-package-by-using-twine

1. Update the package version in `setup.py`. Otherwise, the push will fail with duplicate version number.

2. Install the python `build` and `twine` package:
```
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```

3. Build the common package:
```
python3 -m build
```

Now you will see two more folder generated under ./common/
```
|- common.egg-info/
|- dist/
```

4. Push to GitLab:
```
TWINE_PASSWORD=<PASS>  TWINE_USERNAME=<USER> python3 -m twine upload --repository-url https://git.indocresearch.org/api/v4/projects/158/packages/pypi dist/*
```
