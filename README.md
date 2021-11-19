# Backend app

## Dependencies installation

You need to have a database in the project or elsewhere outsite of the project.

If you do not have a datebase already running, you can create it in the project by running:

```
oc new-app postgresql-persistent --name=postresql -n <project namespace>
```

Copy the template of the secret yaml file `backend.Secret.yaml.template` into `backend.Secret.yaml` and update the fields correctly for your environment. (You can take values from `postgresql` secret from the cluster, if you deploy a new database by using the previous command)

Port forward access to the postgresql pod by running:

```
oc port-forward postgresql-<generated number> 5432:5432
```

and then apply scripts from the `/scripts` folder to create a schema together with default data.
