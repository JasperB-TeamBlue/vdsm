# SPDX-FileCopyrightText: oVirt Developers
# SPDX-License-Identifier: GPL-2.0-or-later

import threading

thread_vars = threading.local()
thread_vars.task = None
thread_vars.context = None
