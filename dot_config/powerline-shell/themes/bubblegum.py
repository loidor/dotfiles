from powerline_shell.themes.default import DefaultColor

"""
colors from https://www.nordtheme.com/docs/colors-and-palettes
"""

#white           = 255
#bubblegum-light = 204
#bubblegum       = 198
night0 = 236 # nord0
night1 = 237 # nord1
night2 = 238 # nord2
night3 = 239 # nord3
snow0  = 253 # nord4
snow1  = 254 # nord5
snow2  = 255 # nord6
frost0 = 109 # ord7
frost1 = 111 # nord8
frost2 = 110 # nord9
frost3 = 68  # nord10
red    = 167 # nord11
orange = 173 # nord12
yellow = 179 # nord13
green  = 150 # nord14
purple = 139 # nord15

class Color(DefaultColor):
    USERNAME_BG = 204
    USERNAME_FG = 255

    HOSTNAME_BG = 198
    HOSTNAME_FG = 255

    HOME_BG = frost3
    HOME_FG = 255
    PATH_BG = 198
    PATH_FG = 255
    CWD_FG = 255
    SEPARATOR_FG = 89

    READONLY_BG = red
    READONLY_FG = 255

    SSH_BG = 255
    SSH_FG = 161

    REPO_CLEAN_BG = green
    REPO_CLEAN_FG = night1
    REPO_DIRTY_BG = red
    REPO_DIRTY_FG = 255

    JOBS_FG = frost3
    JOBS_BG = night0

    #CMD_PASSED_BG = 
    CMD_PASSED_FG = 255
    CMD_FAILED_BG = yellow
    CMD_FAILED_FG = 255

    SVN_CHANGES_BG = REPO_DIRTY_FG
    SVN_CHANGES_FG = REPO_DIRTY_BG

    GIT_AHEAD_BG = night3
    GIT_AHEAD_FG = snow0
    GIT_BEHIND_BG = night3
    GIT_BEHIND_FG = snow0

    GIT_STAGED_BG = frost0
    GIT_STAGED_FG = night1
    GIT_NOTSTAGED_BG = orange
    GIT_NOTSTAGED_FG = 255
    GIT_UNTRACKED_BG = purple
    GIT_UNTRACKED_FG = 255
    GIT_CONFLICTED_BG = red
    GIT_CONFLICTED_FG = 255

    GIT_STASH_BG = yellow
    GIT_STASH_FG = night1

    VIRTUAL_ENV_BG = green
    VIRTUAL_ENV_FG = night1

    BATTERY_NORMAL_BG = green
    BATTERY_NORMAL_FG = night1
    BATTERY_LOW_BG = red
    BATTERY_LOW_FG = 255

    AWS_PROFILE_FG = frost3
    AWS_PROFILE_BG = night0

    TIME_BG = night3
    TIME_FG = 255
