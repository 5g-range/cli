"""
-*- coding: utf-8 -*-

Created in November, 2019
Author: Yuri Moyses

For more information on the click access library: https://click.palletsprojects.com/en/7.x
For more information about the socket access library: https://docs.python.org/pt-br/3/library/socket.html
For more information about the sys access library: https://docs.python.org/3/library/sys.html
For more information about the ctypes access library: https://docs.python.org/3/library/ctypes.html
"""

import sys
import click
from ctypes import *
import socket

# Socket
server_addr = ('localhost', 2300)  # Port and host values
# Create a new socket using the given address family, socket type and protocol number.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_addr)

except socket.error as err:
    print("Socket created falied with error %s" % err)
    sys.exit(0)


class Cli(Structure):
    # Commands
    buff_macStart = 'A'
    buff_macStop = 'B'
    buff_macConfig = "C"
    buff_sets = 'D'
    buff_get = 'E'

    # Atributo
    buff_FusionLUT = 'A'
    buff_uplink = 'B'
    buff_DownlinkMCS = 'C'
    buff_UplinkMCS = 'D'
    buff_MIMOConf = 'E'
    buff_MIMODivMult = 'F'
    buff_MIMOAntena = 'G'
    buff_MIMOPrec = 'H'
    buff_MIMOolcl = 'I'
    buff_TPC = 'J'
    buff_RxMetricsPeriodicity = 'K'


"""
ARGUMENTS OF THE COMMAND GET
"""


def get_FusionLUT(argument, msg):
    cli_out = Cli()
    click.echo("\nSending...")

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_FusionLUT.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nFusionLUT=>%s' % cli_in.FusionLUT)


def get_uplinkreservation(argument, msg):
    cli_out = Cli()
    click.echo("\nSending...")

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_uplink.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')  # And value received


def get_DownlinkMCS(argument, msg):
    cli_out = Cli()
    click.echo("\nSending...")

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_DownlinkMCS.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nDownlinkMCS=>%s' % cli_in.DownlinkMCS)


def get_UplinkMCS(argument, msg):
    cli_out = Cli()
    click.echo("\nSending...")

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_UplinkMCS.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nUplink MCS=>%s' % cli_in.UplinkMCS)


def get_MIMOConf(argument, msg):
    cli_out = Cli()
    click.echo("\nSending {}...".format(argument))

    s.sendto(cli_out.buff_get, server_addr)
    s.sendto(cli_out.buff_MIMOConf)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nMIMOConf=>%s' % cli_in.MIMOConf)


def get_MIMODivMult(argument, msg):
    cli_out = Cli()
    click.echo("\nSending {}...".format(argument))

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buf_MIMODivMult.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nMIMODivMult=>%s' % cli_in.MIMODivMult)


def get_MIMOAntenna(argument, msg):
    cli_out = Cli()
    click.echo("\nSending {}...".format(argument))

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_MIMOAntena.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nMIMOAntenna=>%s' % cli_in.MIMOAntenna)


def get_MIMOPrec(argument, msg):
    cli_out = Cli()
    click.echo("\nSending {}...".format(argument))

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_MIMOPrec.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nMIMOPrec=>%s' % cli_in.MIMOPrec)


def get_MIMOolcl(argument, msg):
    cli_out = Cli()
    click.echo("\nSending {}...}".format(argument))

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_MIMOolcl.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nMIMOolcl=>%s' % cli_in.MIMOolcl)


def get_TPC(argument, msg):
    cli_out = Cli()
    click.echo("\nSending {}...".format(argument))
    nsent = s.send(cli_out)

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_TPC.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nTPC=>%s' % cli_in.TPC)


def get_RxMetricsPeriodicity(argument, msg_):
    cli_out = Cli()
    click.echo("\nSending {}...".format(argument))

    s.sendto(cli_out.buff_get.encode(), server_addr)
    s.sendto(cli_out.buff_RxMetricsPeriodicity.encode(), server_addr)
    s.sendto(msg_.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nRxMetricsPeriodicity=>%s' % cli_in.RxMetricsPeriodicity)


"""
ARGUMENTO DO COMMANDO SET
"""


def set_FusionLUT(argument, ueid):
    cli_out = Cli()
    msg = chr(ueid)
    click.echo("\nSending set =>%s\nSending {}=>%s\nUeid=>%s".format(argument) % (
        cli_out.buff_sets, cli_out.buff_FusionLUT, ueid))
    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_FusionLUT.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


def set_uplinkreservation(argument, ueid, rbstart, numrb):
    if ueid is not None and numrb is not None and rbstart is not None:
        cli_out = Cli()
        msg = chr(ueid) + chr(numrb) + chr(rbstart)
        click.echo("\nSending set =>%s\nSending {}=>%s\nUeid=>%s NumRB=>%s RBStart=>%s".format(argument) %
                   (cli_out.buff_sets, cli_out.buff_uplink,
                    ueid, numrb, rbstart))
        s.sendto(cli_out.buff_sets.encode(), server_addr)
        s.sendto(cli_out.buff_uplink.encode(), server_addr)
        s.sendto(msg.encode('utf-8'), server_addr)

        buff = s.recv(sizeof(Cli))
        cli_in = Cli.from_buffer_copy(buff)
        if not buff:
            click.echo("\nFail")
            click.pause(info='\nPress any key to continue...')
        else:
            click.echo('\nSuccess')
    elif ueid is None:
        click.echo("\nERROR: Value for UEid is {}".format(ueid))
    elif numrb is None:
        click.echo("\nERROR: Value for NumRB is {}".format(numrb))
    elif rbstart is None:
        click.echo("\nERROR: Value for RBStart is {}".format(rbstart))
    elif argument != 'uplinkreservation':
        click.echo("\nERROR: Argument Invalid {}\n".format(argument))
    click.pause(info='\nPress any key to continue...')


def set_MIMOConf(argument, ueid, mimoconf):
    cli_out = Cli()
    msg = chr(ueid) + chr(mimoconf)
    click.echo("\nSending... ")

    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_MIMOConf.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


def set_MIMODivMult(argument, ueid, mimodiv):
    cli_out = Cli()
    msg = chr(ueid) + chr(mimodiv)
    click.echo("\nSending... ")
    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_MIMODivMult.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


def set_MIMOAntenna(argument, ueid, mimoantena):
    cli_out = Cli()
    msg = chr(ueid) + chr(mimoantena)
    click.echo("\nSending... ")

    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_MIMOAntena.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


def set_MIMOolcl(argument, ueid, mimoolcl):
    cli_out = Cli()
    msg = chr(ueid) + chr(mimoolcl)
    click.echo("\nSending... ")

    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_MIMOolcl.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


def set_RxMetricsPeriodicity(argument, rx):
    cli_out = Cli()
    msg = chr(rx)
    click.echo("\nSending... ")
    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_RxMetricsPeriodicity.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


def set_TPC(argument, ueid, tpc):
    cli_out = Cli()
    msg = chr(ueid) + chr(tpc)
    click.echo("\nSending... ")
    s.sendto(cli_out.buff_sets.encode(), server_addr)
    s.sendto(cli_out.buff_TPC.encode(), server_addr)
    s.sendto(msg.encode('utf-8'), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo('\nSuccess')


CONTEXT_SETTINGS = dict(help_option_names=['--help', '-h', '-help', '--h'])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version='0.01', prog_name='CLI 5G RANGE')
def cli():
    """
    CLI 5G RANGE
    """
    pass


@cli.command('sets', help='Dynamic parameters configuration issued only on the BS side;')
@click.argument('argument', type=str)
@click.option('--ueid', type=click.IntRange(0, 12), nargs=1)
@click.option('--numrb', type=click.IntRange(0, 132), nargs=1)
@click.option('--rbstart', type=click.IntRange(0, 132), nargs=1)
@click.option('--mimoconf', type=click.IntRange(0, 1), help='MIMO configuration. MIMO/SISO.')
@click.option('--mimodiv', type=click.IntRange(0, 1), help='MIMO configuration. MIMO Diversidade/Multiplexação.')
@click.option('--mimoantena', type=click.IntRange(0, 1), help='MIMO configuration. MIMO 2x2, 4x4.')
@click.option('--mimoolcl', type=click.IntRange(0, 1), help='MIMO configuration. Open Loop (OL) or Closed Loop (CL)')
@click.option('--rx', type=click.IntRange(0, 10), help='CSI Periodic for CQI, PMI, RI, and SSM in number of subframes')
@click.option('--tpc', type=click.IntRange(0, 40), help='UL Transmission Power Control (TPC) in dBm')
def sets(argument, ueid, numrb, rbstart, mimoconf, mimodiv, mimoantena, mimoolcl, rx, tpc):
    if argument == 'FusionLUT':
        set_FusionLUT(argument, ueid)

    elif argument == 'uplinkreservation':
        set_uplinkreservation(argument, ueid, rbstart, numrb)

    elif argument == 'MIMOConf':
        try:
            set_MIMOConf(argument, ueid, mimoconf)
        except:
            if ueid is None or mimoconf is None:
                click.echo(
                    "\nERROR: Some values may be missing (UEid is {} and MIMOConf is {})\n".format(ueid, mimoconf))

    elif argument == 'MIMODivMult':
        try:
            set_MIMODivMult(argument, ueid, mimodiv)
        except:
            if ueid is None or mimodiv is None:
                click.echo(
                    "\nERROR: Some values may be missing (UEid is {} and MIMODivMult is {})\n".format(ueid, mimodiv))

    elif argument == 'MIMOAntena':
        try:
            set_MIMOAntenna(argument, ueid, mimoantena)
        except:
            if ueid is None or mimoantena is None:
                click.echo(
                    "\nERROR: Some values may be missing (UEid is {} and MIMOAntena is {})\n".format(ueid, mimoantena))

    elif argument == 'MIMOolcl':
        try:
            set_MIMOolcl(argument, ueid, mimoolcl)
        except:
            if ueid is None or mimoolcl is None:
                click.echo(
                    "\nERROR: Some values may be missing (UEid is {} and MIMOolcl is {})\n".format(ueid, mimoolcl))

    elif argument == 'RxMetricsPeriodicity':
        try:
            set_RxMetricsPeriodicity(argument, rx)
        except:
            if rx is None:
                click.echo("\nERROR: Value of {} is {}\n".format(argument, rx))

    elif argument == 'TPC':
        try:
            set_TPC(argument, ueid, tpc)
        except:
            if ueid is None or tpc is None:
                click.echo("\nERROR: Some values may be missing (UEid is {} and TPC is {})\n".format(ueid, tpc))
    else:
        click.echo("\nERROR: Value for argument is wrong ({})\n".format(argument))
        click.pause(info='Press any key to continue...')


# def DownlinkMCS():

# def UplinkMCS():

# def set_MIMOPrec():

"""
COMMAND GET
"""


@cli.command('get', short_help='')
@click.argument('argument', type=str)
@click.option('--rx', '-rx', type=click.IntRange(0, 10),
              help='CSI Periodic for CQI, PMI, RI, and SSM in number of subframes')
@click.option('--ueid', '-ueid', type=click.IntRange(0, 12), required=False)
def get(argument, ueid, rx):  # Ainda falta adicionar os parametros de cada argumento
    try:
        if argument == 'FusionLUT':
            msg = chr(ueid)  # Value of the ueID converted for string
            get_FusionLUT(argument, msg)

        elif argument == 'uplinkreservation':
            msg = chr(ueid)  # Value of the ueID converted for string
            get_uplinkreservation(argument, msg)

        elif argument == 'DownlinkMCS':
            msg = chr(ueid)
            get_DownlinkMCS(argument, msg)

        elif argument == 'UplinkMCS':
            msg = chr(ueid)
            get_UplinkMCS(argument, msg)

        elif argument == 'MIMOConf':
            msg = chr(ueid)
            get_MIMOConf(argument, msg)

        elif argument == 'MIMODivMult':
            msg = chr(ueid)
            get_MIMODivMult(argument, msg)

        elif argument == 'MIMOAntenna':
            msg = chr(ueid)
            get_MIMOAntenna(argument, msg)

        elif argument == 'MIMOPrec':
            msg = chr(ueid)
            get_MIMOPrec(argument, msg)

        elif argument == 'MIMOolcl':
            msg = chr(ueid)
            get_MIMOolcl(argument, msg)

        elif argument == 'TPC':
            msg = chr(ueid)
            get_TPC(argument, msg)
    except:
        click.echo("\nERROR: Value of the UEid is {}\n".format(ueid))

    try:
        if argument == 'RxMetricsPeriodicity':
            msg_ = chr(rx)  # Value of the RxMetrics converted for string
            get_RxMetricsPeriodicity(argument, msg_)
    except:
        if rx is None:
            click.echo("\nERROR: Value of the RxMetricsPeriodicity is {}\n".format(rx))
        else:
            click.echo("\nERROR: Value for argument is wrong ({})\n".format(argument))
            click.pause(info='\nPress any key to continue...')


"""
COMMANDS MAC
"""
@cli.command('macStartRequest', help='')
def macStartRequest():
    cli_out = Cli()
    click.echo("\nSending macStart.Request...")
    s.sendto(cli_out.buff_macStart.encode(), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
    else:
        click.echo("\nReceived macStart.Response => %s" % cli_in.buff_macStart)
    click.pause(info='\nPress any key to continue...')


@cli.command('macConfigRequest', help='MAC Initialization and Static configuration parameter')
def macConfigRequest():
    cli_out = Cli()
    click.echo("\nSending macConfig.Request...")
    s.sendto(cli_out.buff_macConfig.encode(), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo("\nReceived macConfig.Response => %s" % cli_in.buff_macConfig)
    click.pause(info='\nPress any key to continue...')


@cli.command('macStopRequest', help='MAC termination')
def macStopRequest():
    cli_out = Cli()
    click.echo("\nSending macStop.Request...")
    s.sendto(cli_out.buff_macStop.encode(), server_addr)

    buff = s.recv(sizeof(Cli))
    cli_in = Cli.from_buffer_copy(buff)
    if not buff:
        click.echo("\nFail")
        click.pause(info='\nPress any key to continue...')
    else:
        click.echo("\nReceived macStop.Response => %s" % cli_in.buff_macStop)
    click.pause(info='\nPress any key to continue...')


if __name__ == '__main__':
    cli()
