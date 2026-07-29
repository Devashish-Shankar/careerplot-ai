"""
==========================================================
CareerPilot AI

Shared Package

Utilities

Author: Devashish Shankar
==========================================================
"""

from .datetime import (
    add_days,
    add_hours,
    add_minutes,
    add_seconds,
    age_in_days,
    days_from_now,
    duration,
    from_iso,
    hours_from_now,
    is_expired,
    minutes_from_now,
    seconds_from_now,
    to_iso,
    utc_now,
    utc_today,
)
from .filesystem import (
    delete_file,
    directory_exists,
    ensure_directory,
    file_exists,
    file_size,
    list_files,
    read_bytes,
    read_text,
    write_bytes,
    write_text,
)
from .hashing import (
    file_sha256,
    file_sha512,
    md5,
    sha256,
    sha512,
    verify_sha256,
)
from .import_utils import (
    import_module,
    import_object,
)
from .inspect import (
    docstring,
    function_name,
    is_async,
    signature,
)
from .json import (
    dump_json,
    is_valid_json,
    load_json,
    minify_json,
    pretty_json,
)
from .random import (
    random_digits,
    random_hex,
    random_string,
    random_urlsafe,
)
from .reflection import (
    class_name,
    get_attribute,
    has_attribute,
    module_name,
    qualified_name,
)
from .retry import (
    exponential_backoff,
    retry,
)
from .strings import (
    camel_case,
    ends_with_ignore_case,
    equals_ignore_case,
    is_blank,
    kebab_case,
    normalize,
    pascal_case,
    remove_whitespace,
    slugify,
    snake_case,
    starts_with_ignore_case,
    truncate,
)
from .url import (
    add_query_params,
    is_secure_url,
    join_url,
    query_params,
    strip_query,
)
from .validation import (
    is_email,
    is_github_url,
    is_linkedin_url,
    is_phone,
    is_url,
    is_uuid,
)
from .version import (
    executable,
    platform_name,
    platform_release,
    python_implementation,
    python_version,
)

__all__ = [
    # datetime
    "add_days",
    "add_hours",
    "add_minutes",
    "add_seconds",
    "age_in_days",
    "days_from_now",
    "duration",
    "from_iso",
    "hours_from_now",
    "is_expired",
    "minutes_from_now",
    "seconds_from_now",
    "to_iso",
    "utc_now",
    "utc_today",
    # filesystem
    "delete_file",
    "directory_exists",
    "ensure_directory",
    "file_exists",
    "file_size",
    "list_files",
    "read_bytes",
    "read_text",
    "write_bytes",
    "write_text",
    # hashing
    "file_sha256",
    "file_sha512",
    "md5",
    "sha256",
    "sha512",
    "verify_sha256",
    # import_utils
    "import_module",
    "import_object",
    # inspect
    "docstring",
    "function_name",
    "is_async",
    "signature",
    # json
    "dump_json",
    "is_valid_json",
    "load_json",
    "minify_json",
    "pretty_json",
    # random
    "random_digits",
    "random_hex",
    "random_string",
    "random_urlsafe",
    # reflection
    "class_name",
    "get_attribute",
    "has_attribute",
    "module_name",
    "qualified_name",
    # retry
    "exponential_backoff",
    "retry",
    # strings
    "camel_case",
    "ends_with_ignore_case",
    "equals_ignore_case",
    "is_blank",
    "kebab_case",
    "normalize",
    "pascal_case",
    "remove_whitespace",
    "slugify",
    "snake_case",
    "starts_with_ignore_case",
    "truncate",
    # url
    "add_query_params",
    "is_secure_url",
    "join_url",
    "query_params",
    "strip_query",
    # validation
    "is_email",
    "is_github_url",
    "is_linkedin_url",
    "is_phone",
    "is_url",
    "is_uuid",
    # version
    "executable",
    "platform_name",
    "platform_release",
    "python_implementation",
    "python_version",
]
