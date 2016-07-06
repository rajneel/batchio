#
# Cookbook Name:: batchio-python
# Recipe:: default
#
# Copyright 2016, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

include_recipe "yum-ius::default"

python_runtime 'batchio' do
  version '3'
  provider 'system'
  options ({
    'package_name' => 'python35u',
    'package_upgrade' => true,
    'pip_version' => false,
    'setuptools_version' => false,
    'virtualenv_version' => false,
    'wheel_version' => false
  })
end

python_virtualenv 'batchio' do
  python '/usr/bin/python3.5'
  path '/var/lib/batchio/virtualenv'
end

python_package 'PyYAML' do
  action :upgrade
end

# Needed to compile pyzmq which links against libzmq
# package 'gcc-c++' do
#   action :upgrade
# end
#
# package 'zeromq' do
#   action :upgrade
# end
# python_package 'pyzmq' do
#   action :upgrade
#   virtualenv 'batchio'
# end
# python_package 'aiozmq' do
#   action :upgrade
#   virtualenv 'batchio'
# end

python_package 'aiohttp' do
  action :upgrade
end

python_package 'APScheduler' do
  action :upgrade
  virtualenv 'batchio'
end

python_package 'SQLAlchemy' do 
  action :upgrade
  virtualenv 'batchio'
end

python_package 'marshmallow' do
  action :upgrade
  virtualenv 'batchio'
end