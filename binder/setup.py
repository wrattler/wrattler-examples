import setuptools

setuptools.setup(
  name="wrattler-services",
  py_modules=['setup_services'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'pythonservice = setup_services:setup_pythonservice',
          'client = setup_services:setup_client',
          'rservice = setup_services:setup_rservice',
          'datastore = setup_services:setup_datastore',
      ]
  },
  install_requires=['jupyter-server-proxy'],
)
