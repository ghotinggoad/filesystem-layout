def to_lvs(vdisks):
    lvs = {
        persistent_mount_name: {**persistent_mount, "vdisk_name": vdisk_name}
        for vdisk_name, vdisk in vdisks.items()
        for persistent_mount_name, persistent_mount in vdisk.get(
            "persistent_mounts"
        ).items()
    }
    return lvs


class FilterModule(object):
    def filters(self):
        return {"to_lvs": to_lvs}
