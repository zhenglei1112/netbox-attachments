from netbox.plugins import PluginMenu, PluginMenuItem

menu = PluginMenu(
    label="附件管理",
    icon_class="mdi mdi-paperclip",
    groups=(
        (
            "",
            (
                PluginMenuItem(
                    link="plugins:netbox_attachments:netboxattachment_list",
                    link_text="附件",
                    permissions=["netbox_attachments.view_netboxattachment"],
                ),
            ),
        ),
    ),
)
