from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from supabase import (
    create_client,
    Client,  
    SupabaseAuthClient,
    SupabaseRealtimeClient,
    SupabaseStorageClient,

)

from postgrest import (
    SyncPostgrestClient,
    AsyncPostgrestClient,
)


def pytest_configure(config) -> None:
    load_dotenv(dotenv_path="tests/tests.env")


@pytest.fixture(scope="session")
def supabase() -> Client:
    url = os.environ.get("SUPABASE_TEST_URL")
    assert url is not None, "Must provide SUPABASE_TEST_URL environment variable"
    key = os.environ.get("SUPABASE_TEST_KEY")
    assert key is not None, "Must provide SUPABASE_TEST_KEY environment variable"
    return create_client(url, key)

@pytest.fixture(scope="session")
def gotrue(supabase: Client) -> SupabaseAuthClient:
    return supabase.auth

@pytest.fixture(scope="session")
def postgrest(supabase: Client) -> SyncPostgrestClient:
    return supabase.postgrest

@pytest.fixture(scope="session")
def realtime(supabase: Client) -> SupabaseRealtimeClient:
    return supabase.realtime

@pytest.fixture(scope="session")
def storage(supabase: Client) -> SupabaseStorageClient:
    return supabase.storage