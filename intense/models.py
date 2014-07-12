
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Slugged, Orderable
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class TextContent(models.Model):
    '''
    An abstract model just holding content
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        abstract = True


class HomePage(Page):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading at the top of the page")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")
    featured_portfolio_header = models.CharField(max_length=100,
                                                 default="Featured work",)
    featured_portfolio_lead = models.TextField(blank=True,
        help_text="Text just under the Recent Works heading")
    our_clients_header = models.CharField(max_length=100,
                                          default="Our clients")
    our_clients_lead = models.TextField(blank=True,
        help_text="Text just under the Our Clients heading")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Slide(Orderable, TextContent):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    link = models.CharField(max_length=2000, blank=True,
        help_text="If present the title will link here")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("vital_theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)


class IconBox(Orderable, TextContent):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="boxes")
    icon = models.CharField(max_length=50,
        help_text="Enter the name of a font awesome icon, i.e. "
                  "icon-bullhorn. A list is available here "
                  "http://fortawesome.github.io/Font-Awesome/icons/")
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the box will go here.")


class Client(Orderable):
    '''
    A client on the home page
    '''
    name = models.CharField(max_length=200)
    homepage = models.ForeignKey(HomePage, related_name="clients")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("vital_theme.Client.image", "clients"),
        format="Image", max_length=255, null=True, blank=True)
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the logo will go here.")


COLUMNS_CHOICES = (
    ('6', 'Two columns'),
    ('4', 'Three columns'),
    ('3', 'Four Columns'),
)


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    columns = models.CharField(max_length=1, choices=COLUMNS_CHOICES,
        default='3')
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")


class PortfolioItem(Page, RichText):
    '''
    An individual portfolio item, should be nested under a Portfolio
    '''
    subheading = models.CharField(max_length=200, blank=True)
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("nuro_proj.PortfolioItem.featured_image", "portfolio"),
        format="Image", max_length=255, null=True, blank=True)
    short_description = models.TextField(blank=True)
    categories = models.ManyToManyField("PortfolioItemCategory",
                                        verbose_name=_("Categories"),
                                        blank=True,
                                        related_name="portfolioitems")
    client_description = RichTextField(blank=True)
    href = models.CharField(max_length=2000, blank=True,
        help_text="A link to the finished project (optional)")
    related_items = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio items")


class PortfolioItemImage(Orderable):
    '''
    An image for a PortfolioItem
    '''
    portfolioitem = models.ForeignKey(PortfolioItem, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("vital_theme.PortfolioItemImage.file", "portfolio items"))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class PortfolioItemCategory(Slugged):
    """
    A category for grouping portfolio items into a series.
    """

    class Meta:
        verbose_name = _("Portfolio Item Category")
        verbose_name_plural = _("Portfolio Item Categories")
        ordering = ("title",)
