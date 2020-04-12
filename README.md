# Ansible Role Platform

![Molecule Test](https://github.com/ctorgalson/ansible-role-platform/workflows/Molecule%20Test/badge.svg)

This role idempotently installs the [platform.sh cli tool](https://docs.platform.sh/development/cli.html) on Ubuntu/Debian systems.

Specifically, the role performs the following tasks:

1. Clones the platform.sh cli repo in to a user directory,
2. Runs the platform.sh cli installer,
3. Removes the cloned repository,
4. Runs `platform self:update`.

## Role Variables

All of the following variables can be set, but _only_ `psh_user` is mandatory.

| Variable name | Default value | Description |
|---------------|---------------|-------------|
| `psh_user`         | `example` | The user to install the cli tool for. |
| `psh_user_home`    | `/home/{{ psh_user }}` | The path to the user's home directory. Should not normally need changing. |
| `psh_user_shell`   | `/bin/bash` | Path to the user's shell. |
| `psh_user_rc_file` | `{{ psh_user_home }}/.bashrc` | The rc file to add platform.sh cli configuration to. |
| `psh_repo`         | `https://github.com/platformsh/platformsh-cli.git` | The github url to the repository. Should seldom need changing. |
| `psh_dest`         | `{{ psh_user_home }}/platformsh-cli` | The temporary location for the repository on the remote system. |
| `psh_bin`          | `{{ psh_user_home }}/.platformsh/bin/platform` | The path to the `platform` binary, post-install. |

## Example Playbook

    ---
    - name: Install platformsh-cli tool.
      hosts: all
      vars:
        psh_user: "molecule"
      tasks:
        - name: "Include ansible-role-platform"
          include_role:
            name: "ansible-role-platform"

## License

GPLv2

## Author Information

Christopher Torgalson
