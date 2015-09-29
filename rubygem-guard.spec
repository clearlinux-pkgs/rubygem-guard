#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-guard
Version  : 2.13.0
Release  : 6
URL      : https://rubygems.org/downloads/guard-2.13.0.gem
Source0  : https://rubygems.org/downloads/guard-2.13.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-guard-bin
BuildRequires : ruby
BuildRequires : rubygem-formatador
BuildRequires : rubygem-pry
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-thor

%description
:exclamation::exclamation: Guard is [currently accepting more maintainers/contributors](https://groups.google.com/forum/#!topic/guard-dev/2Td0QTvTIsE). :exclamation::exclamation:

%package bin
Summary: bin components for the rubygem-guard package.
Group: Binaries

%description bin
bin components for the rubygem-guard package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n guard-2.13.0
gem spec %{SOURCE0} -l --ruby > rubygem-guard.gemspec

%build
gem build rubygem-guard.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
guard-2.13.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/guard-2.13.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/ArubaAdapter/cdesc-ArubaAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/ArubaAdapter/execute%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/ArubaAdapter/execute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/ArubaAdapter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/cdesc-CLI.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/init-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/notifiers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/show-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/CLI/version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/Bundler/cdesc-Bundler.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/Bundler/verify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/EvaluateOnly/cdesc-EvaluateOnly.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/EvaluateOnly/evaluate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/EvaluateOnly/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/Valid/cdesc-Valid.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/Valid/initialize_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/Valid/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/Valid/start_guard-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/Environments/cdesc-Environments.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Cli/cdesc-Cli.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/cdesc-Commander.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/pause-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/reload-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/run_all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/show-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commander/stop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/All/cdesc-All.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/All/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/All/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Change/cdesc-Change.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Change/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Change/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Notification/cdesc-Notification.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Notification/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Notification/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Pause/cdesc-Pause.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Pause/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Pause/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Reload/cdesc-Reload.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Reload/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Reload/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Scope/cdesc-Scope.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Scope/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Scope/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Show/cdesc-Show.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Show/import-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/Show/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Commands/cdesc-Commands.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Config/cdesc-Config.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Config/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Config/silence_deprecations%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Dsl/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Dsl/ClassMethods/evaluate_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Dsl/add_deprecated-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Dsl/cdesc-Dsl.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Evaluator/add_deprecated-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Evaluator/cdesc-Evaluator.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Evaluator/evaluate_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Evaluator/reevaluate_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/add_group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/add_guard-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/add_plugin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/evaluate_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/evaluator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/fetch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/get_guard_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/groups-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/guard_gem_names-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/guards-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/include%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/keys-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/listener%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/locate_guard-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/lock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/plugin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/reset_evaluator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/runner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/running-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/scope%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/ClassMethods/verify_key%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/add_deprecated-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guard/cdesc-Guard.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guardfile/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guardfile/ClassMethods/create_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guardfile/ClassMethods/initialize_all_templates-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guardfile/ClassMethods/initialize_template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guardfile/add_deprecated-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Guardfile/cdesc-Guardfile.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Watcher/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Watcher/ClassMethods/match_guardfile%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Watcher/add_deprecated-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/Watcher/cdesc-Watcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Deprecated/cdesc-Deprecated.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/_cleanup_backtrace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/callback-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/cdesc-Dsl.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/clearing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/directories-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/evaluate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/filter%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/filter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/guard-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/ignore%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/ignore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/interactor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/notification-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Dsl/watch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslDescriber/_add_row-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslDescriber/cdesc-DslDescriber.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslDescriber/list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslDescriber/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslDescriber/notifiers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslDescriber/show-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/callback-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/cdesc-DslReader.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/clearing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/directories-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/guard-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/ignore%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/ignore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/interactor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/notification-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/plugin_names-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/DslReader/watch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Group/cdesc-Group.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Group/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Group/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Group/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Group/title-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Group/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/NoCustomGuardfile/cdesc-NoCustomGuardfile.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/NoGuardfileError/cdesc-NoGuardfileError.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/NoPluginsError/cdesc-NoPluginsError.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_fetch_guardfile_contents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_from_deprecated-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_guardfile_contents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_guardfile_contents_usable%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_guardfile_contents_without_user_config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_instance_eval_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_read-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_use_default%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_use_inline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/_use_provided-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/cdesc-Evaluator.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/custom%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/evaluate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/guardfile_contents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/guardfile_include%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/guardfile_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/guardfile_source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/inline%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Evaluator/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Generator/_ui-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Generator/cdesc-Generator.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Generator/create_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Generator/initialize_all_templates-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/Generator/initialize_template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Guardfile/cdesc-Guardfile.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/background-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/cdesc-Interactor.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/enabled%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/enabled-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/foreground-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/handle_interrupt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/idle_job-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/interactive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Interactor/options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/_notify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/_reset-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/_trace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/_untrace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/cdesc-Debugging.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/start-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Debugging/stop-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Groups/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Groups/all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Groups/cdesc-Groups.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Groups/matcher_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Groups/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Helpers/_relative_pathname-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Helpers/cdesc-Helpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Plugins/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Plugins/all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Plugins/cdesc-Plugins.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Plugins/matcher_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Plugins/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Plugins/remove-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Queue/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Queue/_run_actions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Queue/cdesc-Queue.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Queue/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Queue/pending%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Queue/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/_find_non_empty_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/_groups-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/_hashify_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/_instantiate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/_scope_names-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/cdesc-Scope.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/from_interactor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/grouped_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/titles-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Scope/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/cdesc-Session.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/clear%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/clearing%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/clearing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/cmdline_groups-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/cmdline_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/convert_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/debug%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/evaluator_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/groups-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_group_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_ignore%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_ignore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_ignore_bang-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_notification%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_plugin_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/guardfile_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/interactor_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/listener_args-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/notify_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/watchdirs%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Session/watchdirs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/State/cdesc-State.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/State/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/State/scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/State/session-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Tracing/cdesc-Tracing.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Tracing/mod;/cdesc-mod;.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Tracing/trace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Tracing/untrace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Traps/cdesc-Traps.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/Traps/handle-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Internals/cdesc-Internals.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Base/background-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Base/foreground-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Base/handle_interrupt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_add_hooks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_add_load_guard_rc_hook-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_add_load_project_guard_rc_hook-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_add_restore_visibility_hook-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_clip_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_configure_prompt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_create_command_aliases-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_create_group_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_create_guard_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_create_run_all_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_kill_pry-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_killed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_prompt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_replace_reset_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_scope_for_prompt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_setup_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/_switch_to_pry-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/background-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/cdesc-PryWrapper.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/foreground-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/handle_interrupt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/PryWrapper/thread-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Sleep/background-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Sleep/cdesc-Sleep.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Sleep/foreground-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/Sleep/handle_interrupt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/TerminalSettings/cdesc-TerminalSettings.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/TerminalSettings/configurable%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/TerminalSettings/echo-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/TerminalSettings/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/TerminalSettings/restore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/TerminalSettings/save-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Jobs/cdesc-Jobs.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Nenv/cdesc-Nenv.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/cdesc-Notifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/connect-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/detected-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/disconnect-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/notify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/supported-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/toggle-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Notifier/turn_on-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Options/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/_register_callbacks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/add_callback-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/callbacks-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/callbacks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/cdesc-Plugin.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/hook-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/non_namespaced_classname-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/non_namespaced_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/notify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/reset_callbacks%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/template-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/title-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Plugin/watchers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/_constant_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/_full_gem_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/_gem_valid%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/_plugin_constant-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/add_to_guardfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/cdesc-PluginUtil.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/initialize_plugin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/plugin_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/plugin_location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/PluginUtil/plugin_names-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/RakeTask/cdesc-RakeTask.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/RakeTask/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/RakeTask/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/RakeTask/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Runner/_run_group_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Runner/_supervise-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Runner/cdesc-Runner.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Runner/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Runner/run_on_changes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Runner/stopping_symbol_for-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Terminal/cdesc-Terminal.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Terminal/clear-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/Colors/cdesc-Colors.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/_filter-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/_filtered_logger_message-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/action_with_scopes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/calling_plugin_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/cdesc-UI.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/clear-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/clearable-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/color-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/color_enabled%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/debug-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/deprecation-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/error-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/info-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/level%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/logger-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/options%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/reset_and_clear-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/reset_line-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/reset_logger-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/UI/warning-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/call_action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/cdesc-Watcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/match_files-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/Watcher/pattern-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/_evaluate-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/_guardfile_deprecated_check-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/_listener_callback-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/_pluginless_guardfile%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/_relative_pathnames-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/_relevant_changes%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/async_queue_add-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/cdesc-Guard.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/init-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/interactor-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/listener-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/queue-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/setup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Guard/state-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Pathname/binwrite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/Pathname/cdesc-Pathname.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-2.13.0/ri/lib/guard/templates/page-Guardfile.ri
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/README.md
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/bin/_guard-core
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/bin/guard
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/images/failed.png
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/images/pending.png
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/images/success.png
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/aruba_adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/cli.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/cli/environments/bundler.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/cli/environments/evaluate_only.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/cli/environments/valid.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commander.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/all.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/change.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/notification.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/pause.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/reload.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/scope.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/commands/show.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/config.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/deprecated/dsl.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/deprecated/evaluator.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/deprecated/guard.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/deprecated/guardfile.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/deprecated/watcher.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/dsl.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/dsl_describer.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/dsl_reader.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/group.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/guardfile.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/guardfile/evaluator.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/guardfile/generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/interactor.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/debugging.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/groups.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/plugins.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/queue.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/scope.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/session.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/state.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/tracing.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/internals/traps.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/jobs/base.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/jobs/pry_wrapper.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/jobs/sleep.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/notifier.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/plugin.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/plugin_util.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/rake_task.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/runner.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/templates/Guardfile
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/terminal.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/ui.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/ui/colors.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/lib/guard/watcher.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/man/guard.1
/usr/lib64/ruby/gems/2.2.0/gems/guard-2.13.0/man/guard.1.html
/usr/lib64/ruby/gems/2.2.0/specifications/guard-2.13.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/_guard-core
/usr/bin/guard
