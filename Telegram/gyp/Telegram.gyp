# This file is part of Telegram Desktop,
# the official desktop version of Telegram messaging app, see https://telegram.org
#
# Telegram Desktop is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# In addition, as a special exception, the copyright holders give permission
# to link the code of portions of this program with the OpenSSL library.
#
# Full license: https://github.com/telegramdesktop/tdesktop/blob/master/LICENSE
# Copyright (c) 2014 John Preston, https://desktop.telegram.org

{
  'includes': [
    'common.gypi',
  ],
  'targets': [{
    'target_name': 'Telegram',
    'variables': {
      'libs_loc': '../../../Libraries',
      'src_loc': '../SourceFiles',
      'res_loc': '../Resources',
      'minizip_loc': '../ThirdParty/minizip',
      'style_files': [
        '<(res_loc)/basic.style',
        '<(res_loc)/basic_types.style',
        '<(src_loc)/boxes/boxes.style',
        '<(src_loc)/dialogs/dialogs.style',
        '<(src_loc)/history/history.style',
        '<(src_loc)/media/view/mediaview.style',
        '<(src_loc)/overview/overview.style',
        '<(src_loc)/profile/profile.style',
        '<(src_loc)/settings/settings.style',
        '<(src_loc)/ui/widgets/widgets.style',
      ],
      'langpacks': [
        'en',
        'de',
        'es',
        'it',
        'nl',
        'ko',
        'pt-BR',
      ],
    },
    'includes': [
      'common_executable.gypi',
      'telegram_qrc.gypi',
      'telegram_win.gypi',
      'telegram_mac.gypi',
      'telegram_linux.gypi',
      'qt.gypi',
      'codegen_rules.gypi',
    ],

    'dependencies': [
      'codegen.gyp:codegen_style',
      'codegen.gyp:codegen_numbers',
      'codegen.gyp:MetaLang',
      'utils.gyp:Updater',
    ],

    'defines': [
      'AL_LIBTYPE_STATIC',
    ],

    'include_dirs': [
      '<(src_loc)',
      '<(SHARED_INTERMEDIATE_DIR)',
      '<(libs_loc)/breakpad/src',
      '<(libs_loc)/lzma/C',
      '<(libs_loc)/libexif-0.6.20',
      '<(libs_loc)/zlib-1.2.8',
      '<(libs_loc)/ffmpeg',
      '<(libs_loc)/openal-soft/include',
      '<(minizip_loc)',
    ],
    'sources': [
      '<@(qrc_files)',
      '<@(style_files)',
      '<(src_loc)/main.cpp',
      '<(src_loc)/stdafx.cpp',
      '<(src_loc)/stdafx.h',
      '<(src_loc)/apiwrap.cpp',
      '<(src_loc)/apiwrap.h',
      '<(src_loc)/app.cpp',
      '<(src_loc)/app.h',
      '<(src_loc)/application.cpp',
      '<(src_loc)/application.h',
      '<(src_loc)/autoupdater.cpp',
      '<(src_loc)/autoupdater.h',
      '<(src_loc)/config.h',
      '<(src_loc)/dialogswidget.cpp',
      '<(src_loc)/dialogswidget.h',
      '<(src_loc)/dropdown.cpp',
      '<(src_loc)/dropdown.h',
      '<(src_loc)/facades.cpp',
      '<(src_loc)/facades.h',
      '<(src_loc)/fileuploader.cpp',
      '<(src_loc)/fileuploader.h',
      '<(src_loc)/history.cpp',
      '<(src_loc)/history.h',
      '<(src_loc)/historywidget.cpp',
      '<(src_loc)/historywidget.h',
      '<(src_loc)/lang.cpp',
      '<(src_loc)/lang.h',
      '<(src_loc)/langloaderplain.cpp',
      '<(src_loc)/langloaderplain.h',
      '<(src_loc)/layerwidget.cpp',
      '<(src_loc)/layerwidget.h',
      '<(src_loc)/layout.cpp',
      '<(src_loc)/layout.h',
      '<(src_loc)/mediaview.cpp',
      '<(src_loc)/mediaview.h',
      '<(src_loc)/observer_peer.cpp',
      '<(src_loc)/observer_peer.h',
      '<(src_loc)/overviewwidget.cpp',
      '<(src_loc)/overviewwidget.h',
      '<(src_loc)/passcodewidget.cpp',
      '<(src_loc)/passcodewidget.h',
      '<(src_loc)/playerwidget.cpp',
      '<(src_loc)/playerwidget.h',
      '<(src_loc)/localimageloader.cpp',
      '<(src_loc)/localimageloader.h',
      '<(src_loc)/localstorage.cpp',
      '<(src_loc)/localstorage.h',
      '<(src_loc)/logs.cpp',
      '<(src_loc)/logs.h',
      '<(src_loc)/mainwidget.cpp',
      '<(src_loc)/mainwidget.h',
      '<(src_loc)/settings.cpp',
      '<(src_loc)/settings.h',
      '<(src_loc)/shortcuts.cpp',
      '<(src_loc)/shortcuts.h',
      '<(src_loc)/structs.cpp',
      '<(src_loc)/structs.h',
      '<(src_loc)/sysbuttons.cpp',
      '<(src_loc)/sysbuttons.h',
      '<(src_loc)/title.cpp',
      '<(src_loc)/title.h',
      '<(src_loc)/mainwindow.cpp',
      '<(src_loc)/mainwindow.h',
      '<(src_loc)/boxes/aboutbox.cpp',
      '<(src_loc)/boxes/aboutbox.h',
      '<(src_loc)/boxes/abstractbox.cpp',
      '<(src_loc)/boxes/abstractbox.h',
      '<(src_loc)/boxes/addcontactbox.cpp',
      '<(src_loc)/boxes/addcontactbox.h',
      '<(src_loc)/boxes/autolockbox.cpp',
      '<(src_loc)/boxes/autolockbox.h',
      '<(src_loc)/boxes/backgroundbox.cpp',
      '<(src_loc)/boxes/backgroundbox.h',
      '<(src_loc)/boxes/confirmbox.cpp',
      '<(src_loc)/boxes/confirmbox.h',
      '<(src_loc)/boxes/confirmphonebox.cpp',
      '<(src_loc)/boxes/confirmphonebox.h',
      '<(src_loc)/boxes/connectionbox.cpp',
      '<(src_loc)/boxes/connectionbox.h',
      '<(src_loc)/boxes/contactsbox.cpp',
      '<(src_loc)/boxes/contactsbox.h',
      '<(src_loc)/boxes/downloadpathbox.cpp',
      '<(src_loc)/boxes/downloadpathbox.h',
      '<(src_loc)/boxes/emojibox.cpp',
      '<(src_loc)/boxes/emojibox.h',
      '<(src_loc)/boxes/languagebox.cpp',
      '<(src_loc)/boxes/languagebox.h',
      '<(src_loc)/boxes/localstoragebox.cpp',
      '<(src_loc)/boxes/localstoragebox.h',
      '<(src_loc)/boxes/passcodebox.cpp',
      '<(src_loc)/boxes/passcodebox.h',
      '<(src_loc)/boxes/photocropbox.cpp',
      '<(src_loc)/boxes/photocropbox.h',
      '<(src_loc)/boxes/photosendbox.cpp',
      '<(src_loc)/boxes/photosendbox.h',
      '<(src_loc)/boxes/report_box.cpp',
      '<(src_loc)/boxes/report_box.h',
      '<(src_loc)/boxes/sessionsbox.cpp',
      '<(src_loc)/boxes/sessionsbox.h',
      '<(src_loc)/boxes/sharebox.cpp',
      '<(src_loc)/boxes/sharebox.h',
      '<(src_loc)/boxes/stickersetbox.cpp',
      '<(src_loc)/boxes/stickersetbox.h',
      '<(src_loc)/boxes/usernamebox.cpp',
      '<(src_loc)/boxes/usernamebox.h',
      '<(src_loc)/core/basic_types.cpp',
      '<(src_loc)/core/basic_types.h',
      '<(src_loc)/core/click_handler.cpp',
      '<(src_loc)/core/click_handler.h',
      '<(src_loc)/core/click_handler_types.cpp',
      '<(src_loc)/core/click_handler_types.h',
      '<(src_loc)/core/lambda_wrap.h',
      '<(src_loc)/core/observer.cpp',
      '<(src_loc)/core/observer.h',
      '<(src_loc)/core/qthelp_url.cpp',
      '<(src_loc)/core/qthelp_url.h',
      '<(src_loc)/core/vector_of_moveable.h',
      '<(src_loc)/data/data_abstract_structure.cpp',
      '<(src_loc)/data/data_abstract_structure.h',
      '<(src_loc)/data/data_drafts.cpp',
      '<(src_loc)/data/data_drafts.h',
      '<(src_loc)/dialogs/dialogs_indexed_list.cpp',
      '<(src_loc)/dialogs/dialogs_indexed_list.h',
      '<(src_loc)/dialogs/dialogs_layout.cpp',
      '<(src_loc)/dialogs/dialogs_layout.h',
      '<(src_loc)/dialogs/dialogs_list.cpp',
      '<(src_loc)/dialogs/dialogs_list.h',
      '<(src_loc)/dialogs/dialogs_row.cpp',
      '<(src_loc)/dialogs/dialogs_row.h',
      '<(src_loc)/history/field_autocomplete.cpp',
      '<(src_loc)/history/field_autocomplete.h',
      '<(src_loc)/history/history_service_layout.cpp',
      '<(src_loc)/history/history_service_layout.h',
      '<(src_loc)/inline_bots/inline_bot_layout_internal.cpp',
      '<(src_loc)/inline_bots/inline_bot_layout_internal.h',
      '<(src_loc)/inline_bots/inline_bot_layout_item.cpp',
      '<(src_loc)/inline_bots/inline_bot_layout_item.h',
      '<(src_loc)/inline_bots/inline_bot_result.cpp',
      '<(src_loc)/inline_bots/inline_bot_result.h',
      '<(src_loc)/inline_bots/inline_bot_send_data.cpp',
      '<(src_loc)/inline_bots/inline_bot_send_data.h',
      '<(src_loc)/intro/introwidget.cpp',
      '<(src_loc)/intro/introwidget.h',
      '<(src_loc)/intro/introcode.cpp',
      '<(src_loc)/intro/introcode.h',
      '<(src_loc)/intro/introphone.cpp',
      '<(src_loc)/intro/introphone.h',
      '<(src_loc)/intro/intropwdcheck.cpp',
      '<(src_loc)/intro/intropwdcheck.h',
      '<(src_loc)/intro/introsignup.cpp',
      '<(src_loc)/intro/introsignup.h',
      '<(src_loc)/intro/introstart.cpp',
      '<(src_loc)/intro/introstart.h',
      '<(src_loc)/media/view/media_clip_controller.cpp',
      '<(src_loc)/media/view/media_clip_controller.h',
      '<(src_loc)/media/view/media_clip_playback.cpp',
      '<(src_loc)/media/view/media_clip_playback.h',
      '<(src_loc)/media/view/media_clip_volume_controller.cpp',
      '<(src_loc)/media/view/media_clip_volume_controller.h',
      '<(src_loc)/media/media_audio.cpp',
      '<(src_loc)/media/media_audio.h',
      '<(src_loc)/media/media_audio_ffmpeg_loader.cpp',
      '<(src_loc)/media/media_audio_ffmpeg_loader.h',
      '<(src_loc)/media/media_audio_loader.cpp',
      '<(src_loc)/media/media_audio_loader.h',
      '<(src_loc)/media/media_audio_loaders.cpp',
      '<(src_loc)/media/media_audio_loaders.h',
      '<(src_loc)/media/media_child_ffmpeg_loader.cpp',
      '<(src_loc)/media/media_child_ffmpeg_loader.h',
      '<(src_loc)/media/media_clip_ffmpeg.cpp',
      '<(src_loc)/media/media_clip_ffmpeg.h',
      '<(src_loc)/media/media_clip_implementation.cpp',
      '<(src_loc)/media/media_clip_implementation.h',
      '<(src_loc)/media/media_clip_qtgif.cpp',
      '<(src_loc)/media/media_clip_qtgif.h',
      '<(src_loc)/media/media_clip_reader.cpp',
      '<(src_loc)/media/media_clip_reader.h',
      '<(src_loc)/mtproto/facade.cpp',
      '<(src_loc)/mtproto/facade.h',
      '<(src_loc)/mtproto/auth_key.cpp',
      '<(src_loc)/mtproto/auth_key.h',
      '<(src_loc)/mtproto/connection.cpp',
      '<(src_loc)/mtproto/connection.h',
      '<(src_loc)/mtproto/connection_abstract.cpp',
      '<(src_loc)/mtproto/connection_abstract.h',
      '<(src_loc)/mtproto/connection_auto.cpp',
      '<(src_loc)/mtproto/connection_auto.h',
      '<(src_loc)/mtproto/connection_http.cpp',
      '<(src_loc)/mtproto/connection_http.h',
      '<(src_loc)/mtproto/connection_tcp.cpp',
      '<(src_loc)/mtproto/connection_tcp.h',
      '<(src_loc)/mtproto/core_types.cpp',
      '<(src_loc)/mtproto/core_types.h',
      '<(src_loc)/mtproto/dcenter.cpp',
      '<(src_loc)/mtproto/dcenter.h',
      '<(src_loc)/mtproto/file_download.cpp',
      '<(src_loc)/mtproto/file_download.h',
      '<(src_loc)/mtproto/rsa_public_key.cpp',
      '<(src_loc)/mtproto/rsa_public_key.h',
      '<(src_loc)/mtproto/rpc_sender.cpp',
      '<(src_loc)/mtproto/rpc_sender.h',
      '<(src_loc)/mtproto/scheme_auto.cpp',
      '<(src_loc)/mtproto/scheme_auto.h',
      '<(src_loc)/mtproto/session.cpp',
      '<(src_loc)/mtproto/session.h',
      '<(src_loc)/overview/overview_layout.cpp',
      '<(src_loc)/overview/overview_layout.h',
      '<(src_loc)/pspecific_win.cpp',
      '<(src_loc)/pspecific_win.h',
      '<(src_loc)/pspecific_mac.cpp',
      '<(src_loc)/pspecific_mac.h',
      '<(src_loc)/pspecific_mac_p.mm',
      '<(src_loc)/pspecific_mac_p.h',
      '<(src_loc)/pspecific_linux.cpp',
      '<(src_loc)/pspecific_linux.h',
      '<(src_loc)/platform/linux/linux_gdk_helper.cpp',
      '<(src_loc)/platform/linux/linux_gdk_helper.h',
      '<(src_loc)/platform/linux/linux_libs.cpp',
      '<(src_loc)/platform/linux/linux_libs.h',
      '<(src_loc)/platform/linux/file_dialog_linux.cpp',
      '<(src_loc)/platform/linux/file_dialog_linux.h',
      '<(src_loc)/platform/linux/main_window_linux.cpp',
      '<(src_loc)/platform/linux/main_window_linux.h',
      '<(src_loc)/platform/mac/main_window_mac.mm',
      '<(src_loc)/platform/mac/main_window_mac.h',
      '<(src_loc)/platform/win/main_window_win.cpp',
      '<(src_loc)/platform/win/main_window_win.h',
      '<(src_loc)/platform/win/windows_app_user_model_id.cpp',
      '<(src_loc)/platform/win/windows_app_user_model_id.h',
      '<(src_loc)/platform/win/windows_dlls.cpp',
      '<(src_loc)/platform/win/windows_dlls.h',
      '<(src_loc)/platform/win/windows_event_filter.cpp',
      '<(src_loc)/platform/win/windows_event_filter.h',
      '<(src_loc)/platform/win/windows_toasts.cpp',
      '<(src_loc)/platform/win/windows_toasts.h',
      '<(src_loc)/profile/profile_actions_widget.cpp',
      '<(src_loc)/profile/profile_actions_widget.h',
      '<(src_loc)/profile/profile_block_widget.cpp',
      '<(src_loc)/profile/profile_block_widget.h',
      '<(src_loc)/profile/profile_cover_drop_area.cpp',
      '<(src_loc)/profile/profile_cover_drop_area.h',
      '<(src_loc)/profile/profile_cover.cpp',
      '<(src_loc)/profile/profile_cover.h',
      '<(src_loc)/profile/profile_fixed_bar.cpp',
      '<(src_loc)/profile/profile_fixed_bar.h',
      '<(src_loc)/profile/profile_info_widget.cpp',
      '<(src_loc)/profile/profile_info_widget.h',
      '<(src_loc)/profile/profile_inner_widget.cpp',
      '<(src_loc)/profile/profile_inner_widget.h',
      '<(src_loc)/profile/profile_invite_link_widget.cpp',
      '<(src_loc)/profile/profile_invite_link_widget.h',
      '<(src_loc)/profile/profile_members_widget.cpp',
      '<(src_loc)/profile/profile_members_widget.h',
      '<(src_loc)/profile/profile_section_memento.cpp',
      '<(src_loc)/profile/profile_section_memento.h',
      '<(src_loc)/profile/profile_settings_widget.cpp',
      '<(src_loc)/profile/profile_settings_widget.h',
      '<(src_loc)/profile/profile_shared_media_widget.cpp',
      '<(src_loc)/profile/profile_shared_media_widget.h',
      '<(src_loc)/profile/profile_userpic_button.cpp',
      '<(src_loc)/profile/profile_userpic_button.h',
      '<(src_loc)/profile/profile_widget.cpp',
      '<(src_loc)/profile/profile_widget.h',
      '<(src_loc)/serialize/serialize_common.cpp',
      '<(src_loc)/serialize/serialize_common.h',
      '<(src_loc)/serialize/serialize_document.cpp',
      '<(src_loc)/serialize/serialize_document.h',
      '<(src_loc)/settings/settings_advanced_widget.cpp',
      '<(src_loc)/settings/settings_advanced_widget.h',
      '<(src_loc)/settings/settings_background_widget.cpp',
      '<(src_loc)/settings/settings_background_widget.h',
      '<(src_loc)/settings/settings_block_widget.cpp',
      '<(src_loc)/settings/settings_block_widget.h',
      '<(src_loc)/settings/settings_chat_settings_widget.cpp',
      '<(src_loc)/settings/settings_chat_settings_widget.h',
      '<(src_loc)/settings/settings_cover.cpp',
      '<(src_loc)/settings/settings_cover.h',
      '<(src_loc)/settings/settings_fixed_bar.cpp',
      '<(src_loc)/settings/settings_fixed_bar.h',
      '<(src_loc)/settings/settings_general_widget.cpp',
      '<(src_loc)/settings/settings_general_widget.h',
      '<(src_loc)/settings/settings_info_widget.cpp',
      '<(src_loc)/settings/settings_info_widget.h',
      '<(src_loc)/settings/settings_inner_widget.cpp',
      '<(src_loc)/settings/settings_inner_widget.h',
      '<(src_loc)/settings/settings_notifications_widget.cpp',
      '<(src_loc)/settings/settings_notifications_widget.h',
      '<(src_loc)/settings/settings_privacy_widget.cpp',
      '<(src_loc)/settings/settings_privacy_widget.h',
      '<(src_loc)/settings/settings_scale_widget.cpp',
      '<(src_loc)/settings/settings_scale_widget.h',
      '<(src_loc)/settings/settings_widget.cpp',
      '<(src_loc)/settings/settings_widget.h',
      '<(src_loc)/ui/buttons/history_down_button.cpp',
      '<(src_loc)/ui/buttons/history_down_button.h',
      '<(src_loc)/ui/buttons/icon_button.cpp',
      '<(src_loc)/ui/buttons/icon_button.h',
      '<(src_loc)/ui/buttons/left_outline_button.cpp',
      '<(src_loc)/ui/buttons/left_outline_button.h',
      '<(src_loc)/ui/buttons/peer_avatar_button.cpp',
      '<(src_loc)/ui/buttons/peer_avatar_button.h',
      '<(src_loc)/ui/buttons/round_button.cpp',
      '<(src_loc)/ui/buttons/round_button.h',
      '<(src_loc)/ui/effects/fade_animation.cpp',
      '<(src_loc)/ui/effects/fade_animation.h',
      '<(src_loc)/ui/style/style_core.cpp',
      '<(src_loc)/ui/style/style_core.h',
      '<(src_loc)/ui/style/style_core_color.cpp',
      '<(src_loc)/ui/style/style_core_color.h',
      '<(src_loc)/ui/style/style_core_font.cpp',
      '<(src_loc)/ui/style/style_core_font.h',
      '<(src_loc)/ui/style/style_core_icon.cpp',
      '<(src_loc)/ui/style/style_core_icon.h',
      '<(src_loc)/ui/style/style_core_types.cpp',
      '<(src_loc)/ui/style/style_core_types.h',
      '<(src_loc)/ui/text/text.cpp',
      '<(src_loc)/ui/text/text.h',
      '<(src_loc)/ui/text/text_block.cpp',
      '<(src_loc)/ui/text/text_block.h',
      '<(src_loc)/ui/text/text_entity.cpp',
      '<(src_loc)/ui/text/text_entity.h',
      '<(src_loc)/ui/toast/toast.cpp',
      '<(src_loc)/ui/toast/toast.h',
      '<(src_loc)/ui/toast/toast_manager.cpp',
      '<(src_loc)/ui/toast/toast_manager.h',
      '<(src_loc)/ui/toast/toast_widget.cpp',
      '<(src_loc)/ui/toast/toast_widget.h',
      '<(src_loc)/ui/widgets/label_simple.cpp',
      '<(src_loc)/ui/widgets/label_simple.h',
      '<(src_loc)/ui/widgets/widget_slide_wrap.h',
      '<(src_loc)/ui/animation.cpp',
      '<(src_loc)/ui/animation.h',
      '<(src_loc)/ui/boxshadow.cpp',
      '<(src_loc)/ui/boxshadow.h',
      '<(src_loc)/ui/button.cpp',
      '<(src_loc)/ui/button.h',
      '<(src_loc)/ui/popupmenu.cpp',
      '<(src_loc)/ui/popupmenu.h',
      '<(src_loc)/ui/countryinput.cpp',
      '<(src_loc)/ui/countryinput.h',
      '<(src_loc)/ui/emoji_config.cpp',
      '<(src_loc)/ui/emoji_config.h',
      '<(src_loc)/ui/filedialog.cpp',
      '<(src_loc)/ui/filedialog.h',
      '<(src_loc)/ui/flatbutton.cpp',
      '<(src_loc)/ui/flatbutton.h',
      '<(src_loc)/ui/flatcheckbox.cpp',
      '<(src_loc)/ui/flatcheckbox.h',
      '<(src_loc)/ui/flatinput.cpp',
      '<(src_loc)/ui/flatinput.h',
      '<(src_loc)/ui/flatlabel.cpp',
      '<(src_loc)/ui/flatlabel.h',
      '<(src_loc)/ui/flattextarea.cpp',
      '<(src_loc)/ui/flattextarea.h',
      '<(src_loc)/ui/images.cpp',
      '<(src_loc)/ui/images.h',
      '<(src_loc)/ui/inner_dropdown.cpp',
      '<(src_loc)/ui/inner_dropdown.h',
      '<(src_loc)/ui/scrollarea.cpp',
      '<(src_loc)/ui/scrollarea.h',
      '<(src_loc)/ui/twidget.cpp',
      '<(src_loc)/ui/twidget.h',
      '<(src_loc)/window/chat_background.cpp',
      '<(src_loc)/window/chat_background.h',
      '<(src_loc)/window/main_window.cpp',
      '<(src_loc)/window/main_window.h',
      '<(src_loc)/window/section_widget.cpp',
      '<(src_loc)/window/section_widget.h',
      '<(src_loc)/window/slide_animation.cpp',
      '<(src_loc)/window/slide_animation.h',
      '<(src_loc)/window/top_bar_widget.cpp',
      '<(src_loc)/window/top_bar_widget.h',
    ],
    'configurations': {
      'Release': {
        'conditions': [
          ['"<(official_build_target)" != ""', {
            'defines': [
              'CUSTOM_API_ID',
            ],
          }],
        ],
      },
    },
    'conditions': [
      [ '"<(official_build_target)" != ""', {
        'dependencies': [
          'utils.gyp:Packer',
        ],
      }],
      [ '"<(build_linux)" != "1"', {
        'sources!': [
          '<(src_loc)/pspecific_linux.cpp',
          '<(src_loc)/pspecific_linux.h',
          '<(src_loc)/platform/linux/linux_gdk_helper.cpp',
          '<(src_loc)/platform/linux/linux_gdk_helper.h',
          '<(src_loc)/platform/linux/linux_libs.cpp',
          '<(src_loc)/platform/linux/linux_libs.h',
          '<(src_loc)/platform/linux/file_dialog_linux.cpp',
          '<(src_loc)/platform/linux/file_dialog_linux.h',
          '<(src_loc)/platform/linux/main_window_linux.cpp',
          '<(src_loc)/platform/linux/main_window_linux.h',
        ],
      }],
      [ '"<(build_mac)" != "1"', {
        'sources!': [
          '<(src_loc)/pspecific_mac.cpp',
          '<(src_loc)/pspecific_mac.h',
          '<(src_loc)/pspecific_mac_p.mm',
          '<(src_loc)/pspecific_mac_p.h',
          '<(src_loc)/platform/mac/main_window_mac.mm',
          '<(src_loc)/platform/mac/main_window_mac.h',
        ],
      }],
      [ '"<(build_win)" != "1"', {
        'sources': [
          '<(minizip_loc)/crypt.h',
          '<(minizip_loc)/ioapi.c',
          '<(minizip_loc)/ioapi.h',
          '<(minizip_loc)/zip.c',
          '<(minizip_loc)/zip.h',
        ],
        'sources!': [
          '<(src_loc)/pspecific_win.cpp',
          '<(src_loc)/pspecific_win.h',
          '<(src_loc)/platform/win/main_window_win.cpp',
          '<(src_loc)/platform/win/main_window_win.h',
          '<(src_loc)/platform/win/windows_app_user_model_id.cpp',
          '<(src_loc)/platform/win/windows_app_user_model_id.h',
          '<(src_loc)/platform/win/windows_dlls.cpp',
          '<(src_loc)/platform/win/windows_dlls.h',
          '<(src_loc)/platform/win/windows_event_filter.cpp',
          '<(src_loc)/platform/win/windows_event_filter.h',
          '<(src_loc)/platform/win/windows_toasts.cpp',
          '<(src_loc)/platform/win/windows_toasts.h',
        ],
      }],
    ],
  }],
}
