# SPDX-FileCopyrightText: oVirt Developers
# SPDX-License-Identifier: GPL-2.0-or-later

from vdsm.network.nmstate.options import BridgeOptsBuilder


def test_parse_nets_bridge_opts():
    nets = {
        'br1': 'multicast_router=0 multicast_snooping=0',
        'br2': 'multicast_router=1 multicast_snooping=1',
    }
    expected = {
        'br1': {
            'multicast-router': 0,
            'multicast-snooping': False,
            'stp': {'enabled': False},
        },
        'br2': {
            'multicast-router': 1,
            'multicast-snooping': True,
            'stp': {'enabled': False},
        },
    }

    for name, opts in nets.items():
        parsed_opts = BridgeOptsBuilder().parse(opts)
        assert expected[name] == parsed_opts
