"""
Functions to start Wrattler services, to be used in entrypoints
that jupyter-server-proxy can use, such that the services are
available via <base_url>/proxy/port/
"""


def setup_pythonservice():
  return {
    'command': ['wrattler-python-service']
  }

def setup_datastore():
  return {
    'command': ['wrattler-data-store']
  }


def setup_rservice():
  return {
    'command': ['Rscript','/wrattler/server/R/app.R']
  }


def setup_client():
  return {
    'command': ['http-server','/wrattler/client/public','-c-1','--cors']
  }


def setup_aiassistants():
  return {
    'command': ['dotnet','/wrattler/aiassistants/server/bin/Debug/netcoreapp2.1/aiassistants.dll']
  }
