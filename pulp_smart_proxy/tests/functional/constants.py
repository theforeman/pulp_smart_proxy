"""Constants for Pulp Smrt plugin tests."""

from urllib.parse import urljoin

from pulp_smash.constants import PULP_FIXTURES_BASE_URL
from pulp_smash.pulp3.constants import (
    BASE_DISTRIBUTION_PATH,
    BASE_PUBLICATION_PATH,
    BASE_REMOTE_PATH,
    BASE_REPO_PATH,
    BASE_CONTENT_PATH,
)

# FIXME: list any download policies supported by your plugin type here.
# If your plugin supports all download policies, you can import this
# from pulp_smash.pulp3.constants instead.
# DOWNLOAD_POLICIES = ["immediate", "streamed", "on_demand"]
DOWNLOAD_POLICIES = ["immediate"]

# FIXME: replace 'unit' with your own content type names, and duplicate as necessary for each type
SMRT_CONTENT_NAME = "smrt.unit"

# FIXME: replace 'unit' with your own content type names, and duplicate as necessary for each type
SMRT_CONTENT_PATH = urljoin(BASE_CONTENT_PATH, "smrt/units/")

SMRT_REMOTE_PATH = urljoin(BASE_REMOTE_PATH, "smrt/smrt/")

SMRT_REPO_PATH = urljoin(BASE_REPO_PATH, "smrt/smrt/")

SMRT_PUBLICATION_PATH = urljoin(BASE_PUBLICATION_PATH, "smrt/smrt/")

SMRT_DISTRIBUTION_PATH = urljoin(BASE_DISTRIBUTION_PATH, "smrt/smrt/")

# FIXME: replace this with your own fixture repository URL and metadata
SMRT_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, "smrt/")
"""The URL to a smrt repository."""

# FIXME: replace this with the actual number of content units in your test fixture
SMRT_FIXTURE_COUNT = 3
"""The number of content units available at :data:`SMRT_FIXTURE_URL`."""

SMRT_FIXTURE_SUMMARY = {SMRT_CONTENT_NAME: SMRT_FIXTURE_COUNT}
"""The desired content summary after syncing :data:`SMRT_FIXTURE_URL`."""

# FIXME: replace this with the location of one specific content unit of your choosing
SMRT_URL = urljoin(SMRT_FIXTURE_URL, "")
"""The URL to an smrt file at :data:`SMRT_FIXTURE_URL`."""

# FIXME: replace this with your own fixture repository URL and metadata
SMRT_INVALID_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, "smrt-invalid/")
"""The URL to an invalid smrt repository."""

# FIXME: replace this with your own fixture repository URL and metadata
SMRT_LARGE_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, "smrt_large/")
"""The URL to a smrt repository containing a large number of content units."""

# FIXME: replace this with the actual number of content units in your test fixture
SMRT_LARGE_FIXTURE_COUNT = 25
"""The number of content units available at :data:`SMRT_LARGE_FIXTURE_URL`."""
