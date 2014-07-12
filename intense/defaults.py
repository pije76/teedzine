
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
        "footer."),
    editable=True,
    default="https://facebook.com/teedzine",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the "
        "footer."),
    editable=True,
    default="https://twitter.com/teedzine",
)

register_setting(
    name="SOCIAL_LINK_GOOGLE",
    label=_("Google Plus link"),
    description=_("If present a Google Plus icon linking here will be in the "
        "footer."),
    editable=True,
    default="https://plus.google.com/b/118069550927850290401/118069550927850290401",
)

register_setting(
    name="SOCIAL_LINK_LINKEDIN",
    label=_("LinkedIn link"),
    description=_("If present a LinkedIn icon linking here will be in the "
        "footer."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_PINTEREST",
    label=_("Pinterest link"),
    description=_("If present a Pinterest icon linking here will be in the "
        "footer."),
    editable=True,
    default="http://www.pinterest.com/teedzine",
)

register_setting(
    name="FLICKR_ID",
    label=_("Flickr ID"),
    description=_("If present a Flickr feed will show in the footer."),
    editable=True,
    default="55925941@N08",
)

register_setting(
    name="ADDRESS",
    label=_("Address"),
    description=_("If present a map will be shown on the contact page with this address"),
    editable=True,
    default="Willis Tower, 233 S Wacker Dr, Chicago, IL 60606",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_GOOGLE",
             "SOCIAL_LINK_LINKEDIN",
             "SOCIAL_LINK_PINTEREST",
             "FLICKR_ID",
             "ADDRESS"),
)