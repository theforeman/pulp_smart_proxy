"""
Check `Plugin Writer's Guide`_ for more details.

.. _Plugin Writer's Guide:
    https://pulpproject.org/pulpcore/docs/dev/
"""

from logging import getLogger

from django.db import models

from pulpcore.plugin.models import (
    Content,
    ContentArtifact,
    Remote,
    Repository,
    Publication,
    Distribution,
)
from pulpcore.plugin.util import get_domain_pk

logger = getLogger(__name__)


class SmrtContent(Content):
    """
    The "smrt" content type.

    Define fields you need for your new content type and
    specify uniqueness constraint to identify unit of this type.

    For example::

        field1 = models.TextField()
        field2 = models.IntegerField()
        field3 = models.CharField()

        class Meta:
            default_related_name = "%(app_label)s_%(model_name)s"
            unique_together = ("field1", "field2")
    """

    TYPE = "smrt"

    name = models.CharField(blank=False, null=False)
    _pulp_domain = models.ForeignKey("core.Domain", default=get_domain_pk, on_delete=models.PROTECT)

    class Meta:
        default_related_name = "%(app_label)s_%(model_name)s"
        unique_together = ("name", "_pulp_domain")


class SmrtPublication(Publication):
    """
    A Publication for SmrtContent.

    Define any additional fields for your new publication if needed.
    """

    TYPE = "smrt"

    class Meta:
        default_related_name = "%(app_label)s_%(model_name)s"


class SmrtRemote(Remote):
    """
    A Remote for SmrtContent.

    Define any additional fields for your new remote if needed.
    """

    TYPE = "smrt"

    class Meta:
        default_related_name = "%(app_label)s_%(model_name)s"


class SmrtRepository(Repository):
    """
    A Repository for SmrtContent.

    Define any additional fields for your new repository if needed.
    """

    TYPE = "smrt"

    CONTENT_TYPES = [SmrtContent]

    class Meta:
        default_related_name = "%(app_label)s_%(model_name)s"


class SmrtDistribution(Distribution):
    """
    A Distribution for SmrtContent.

    Define any additional fields for your new distribution if needed.
    """

    TYPE = "smrt"

    class Meta:
        default_related_name = "%(app_label)s_%(model_name)s"
