### long time ago
    - 4-55 received from R&S. USB/LSB demodulation broken. Downgraded to 4.50.
    - running 4.56 
    - Seldom lock-ups of the receiver, generates humm, no ifpanel or iq streams. Lock-up can be ended with a short test.
### 2016-03-19
    - Downgraded receiver to 4.50.
    - Informed R&D Customer Support, promised to send an answer after easter.
### 2016-04-24
    - upgraded to 4.56 again
    - internal GUI lost connection to receiver, both run, but manual operation does not go through. Remote GUI still works as normal
### 2016-05-01
    - lock-up again, downgraded to 4.50
    - again internal communication loss with error message from gui ;-(
### 2016-05-05
    - CAT5 cable from FP to receiver was not klicked in. Fixed.
### 2016-05-16
    - discovered ftp access in antenna correction factor manual, user: EB500, pwd: EB500
    - also works for telnet, then some consolse commands are available, try "help"
    - "rld" displays a ramlog, monitoring everything that is going on in the receiver
### 2016-06-05
    - what really happens when the front pannel stalls:
        - the receiver still works without problems from remote
        - the ramlog does not show anything special
        - the front panel display follows the receiver
        - input from front panel is ignored
        - after some time, the input is processed
### 2016-06-19
    - now disassembled also the fronst panel PC, cleaned RJ45 connection with air
    - since then, np more drops of eth0 in ramlog, and no more interruptions of internal gui

#### 2016-08-03
    - back to 4.56 on the receiver  (GUI still on 4.50)
    - lockup occurs
    - ramdlog does not show anything special, maybe some dropouts oun eth90
```
    eb500> rld
Displaying ramlog virtual range 0x0 - 0x26af
__RAMLOG_SESSION_START__
exec: Booting OSE5.7 (BL770317)
pvr: 0x80830031
Detected PowerPC e300 core.
exec: nested interrupts enabled
mm: mm_open_exception_area(cpu_descriptor=871018,vector_base=0, vector_size=4000) 
cpu_hal_6xx: init_cpu.
mm: mm_open_exception_area MMU=0
mm: mm_install_exception_handlers: entry
mm: start parsing log_mem string: krn/log_mem/RAM
krn/ramlog:base = 20480 (0x5000)
krn/ramlog:size = 32768 (0x8000)
mm: max_domains:255 @ fd5350
Boot heap automatically configured. [0x15fd7000-0x1fffffff]
init_boot_heap(0x15fd7000, 0x1fffffff)
Initial range : [0x15fd7000-0x1fffffff]
curr_base     : 0x20000000
phys_frag     :
MM:add_bank: name RAM [0000000000000000-0x00000020000000]
   bank_size 0x00000000160035, frag_cnt0x00000000020000,(sizeof *bank) 0x40, (sizeof *frag) 0xb 
mm: phys_mem [0x0000000000000000-0x000000001fffffff] SASE RAM                             
mm: start parsing log_mem string: krn/log_mem/FPGA
mm: log_mem  [0xa0000000-0xa3ffffff]     SASE FPGA 
mm: start parsing log_mem string: krn/log_mem/IO
mm: log_mem  [0xe0000000-0xffffffff]     SASE IO 
mm: start parsing log_mem string: krn/log_mem/RAM
mm: log_mem  [0x00000000-0x1fffffff]     SASE RAM 
mm: region "bcsr": [0xf8000000-0xf8007fff], (0x00008000) su_rw_usr_na inhibited ordered_access
krn/region/bcsr: [0xf8000000-0xf8007fff]
mm: region "code": [0x00010000-0x00847fff], (0x00838000) su_rx_usr_rx copy_back speculative_access
krn/region/code: [0x00010000-0x00847fff]
mm: region "data": [0x00848000-0x15fd6fff], (0x1578f000) su_rw_usr_ro copy_back speculative_access
krn/region/data: [0x00848000-0x15fd6fff]
mm: region "exception": [0x00000000-0x00003fff], (0x00004000) su_rx_usr_na copy_back speculative_access
krn/region/exception: [0x00000000-0x00003fff]
mm: region "flash": [0xfc000000-0xffffffff], (0x04000000) su_rw_usr_na inhibited ordered_access
krn/region/flash: [0xfc000000-0xffffffff]
mm: region "fpga": [0xa0000000-0xa3ffffff], (0x04000000) su_rw_usr_na inhibited ordered_access
krn/region/fpga: [0xa0000000-0xa3ffffff]
mm: region "immr": [0xe0000000-0xe00fffff], (0x00100000) su_rw_usr_na inhibited ordered_access
krn/region/immr: [0xe0000000-0xe00fffff]
mm: region "ramlog": [0x00005000-0x0000cfff], (0x00008000) su_rw_usr_na write_through speculative_access
krn/region/ramlog: [0x00005000-0x0000cfff]
cpu_hal_6xx: enable_caches (1,1)
L1 D cache enabled.
L1 I cache enabled.
mm: map_regions()
MM-meta-data: [0x1fe9c000-0x1fffffff]
MM init completed
mm: initialization completed.
Cache bios installed.
bsp: MPC834x Rev 3.1
exec: memory_model=0 table_extend=12 queued_signal_action=keep
ramtrace tarce_create: buffer: fd6a00 trace: fd6a00, beg: fd6a50 sizeof header: 50
rmm: Trace could not be recovered.
rmm: krn/monitor/sys_error=debug:0
ramtrace tarce_create: buffer: fd6a00 trace: fd6a00, beg: fd6a50 sizeof header: 50
rmm: Up and running. Intercept processes: No.
exec: Creating isr for tick at vector 0, reload=66000
exec: Starting syspool extender.
kernel is up.
zzstart_stack: base 0xfd5948, size 4000, used 3552 (88%)
0.001 core: Core startup of image "EB500-OSE5.7".
0.001 core: Starting HEAP.
core: Using static heap of size 33554432.
0.002 core: Starting DDA device manager.
0.002 core: Installing static device drivers.
devman: Handed over the end-of-interrupt handling to the kernel.
dda: ddamm_alloc_uncached from MM(16384) = 0x15ff7000
devman: Started (log_mask=0x1)
0.003 core: Register driver hostbus.
0.003 core: Register driver mram.
0.003 core: Register driver dma.
0.003 core: Register driver fdma.
0.003 core: Register driver portbus834x.
0.003 core: Register driver cmosram.
0.003 core: Register driver fpps.
0.003 core: Register driver fpga_uart.
0.003 core: Register driver firq.
0.003 core: Register driver fpga_tmr.
0.003 core: Register driver brg_mpc834x.
0.003 core: Register driver pic_ipic.
0.003 core: Register driver timer_gt.
0.003 core: Register driver ud16550.
0.003 core: Register driver spi.
0.003 core: Register driver i2c.
0.003 core: Register driver mii_mpc85xx.
0.003 core: Register driver tsec.
0.003 core: Activating devices.
dda/mpc834x: successfully activated.
dda/mpc834x/i2c1: successfully activated.
dda/mpc834x/i2c2: successfully activated.
dda/mpc834x/mii: successfully activated.
dda/mpc834x/pic: successfully activated.
dda/mpc834x/cmosram: IRQ64 [Falling Edge]
dda/mpc834x/cmosram: successfully activated.
dda/mpc834x/dma: successfully activated.
dda/mpc834x/fdma: IRQ66 [Active Low]
dda/mpc834x/fdma: successfully activated.
dda/mpc834x/fpga_tmr: IRQ66 [Active Low]
dda/mpc834x/fpga_tmr: successfully activated.
dda/mpc834x/fpga_uart: IRQ66 [Active Low]
dda/mpc834x/fpga_uart: successfully activated.
dda/mpc834x/fpps: IRQ67 [Active Low]
dda/mpc834x/fpps: successfully activated.
dda/mpc834x/gt1: timer 0 frequency is 264 MHz
dda/mpc834x/gt1: timer 1 frequency is 264 MHz
dda/mpc834x/gt1: timer 0 is free-running.
dda/mpc834x/gt1: successfully activated.
dda/mpc834x/gt2: timer 0 frequency is 264 MHz
dda/mpc834x/gt2: timer 1 frequency is 264 MHz
dda/mpc834x/gt2: successfully activated.
dda/mpc834x/hostbus: IRQ65 [Falling Edge]
dda/mpc834x/hostbus: successfully activated.
dda/mpc834x/portbus: successfully activated.
dda/mpc834x/spi: successfully activated.
dda/mpc834x/tsec0: TSEC @ 0xe0024000
dda/mpc834x/tsec0: successfully activated.
dda/mpc834x/tsec1: TSEC @ 0xe0025000
dda/mpc834x/tsec1: successfully activated.
dda/mpc834x/uart1: successfully activated.
dda/mpc834x/uart2: successfully activated.
0.012 core: Starting RTC.
0.012 core: Current time Thu Jan  1 00:00:00 1970.
0.012 core: Starting FSS.
0.012 core: Starting SHELLD.
0.013 core: Starting CONFM.
0.013 core: Starting FAM.
0.013 core: Flash area base:0xfc000000 size:0x4000000 driver:cfi params:.
fam_cfi: Driver detected a 16bit device
fam_cfi: cfi driver detected 65536K of flash at 0xfc000000 [00:00]
fam_cfi: Detected command set (0x2)
0.015 core: Starting FLASHFX.
ffxddb:Unit 0: block_size: 512 bytes, nblocks: 31877.
ffxddb:Unit 1: block_size: 512 bytes, nblocks: 47941.
Starting JEFF.
0.026 core: Mounting volume /boot format:jeff device:ffxddb params:unit=0.
CFS: Testing C++ exceptions. If this test fails, the node will most likely crash. If so, make sure the exception table is present.
CFS: OK: Exception handling works well
0.062 core: Mounting volume /user format:jeff device:ffxddb params:unit=1.
CFS: Testing C++ exceptions. If this test fails, the node will most likely crash. If so, make sure the exception table is present.
CFS: OK: Exception handling works well
0.069 core: Core startup complete.
* SearchAndCreateModules (max. 9 <= 40): 40665806,2,0xC7; 40665906,0,0xDF; 40726100,1,0xA0; 40662007,1,0x41; 40726498,1,0x1B; 40726369,1,0x1A;
* Startup receiver start
* Device: EB500-100867-003
7.525 netw: setDHCPHostname = rs-EB500-100867-003.
7.525 core: Starting network supervisor.
7.525 netw: Network startup initiated.
netw: Creating ose_inet
IPCOM: setting log level Warning on IPCOM/IPSTACK
creating '@(#) IPLITE $Name: iplite2-any-r6_8_1 $ - Copyright 2000-2010 Interpeak AB (http://www.interpeak.se). All rights reserved.'creating '@(#) IPPPP $Name: ipppp-any-r6_8_1 $ - Copyright 2000-2010 Interpeak AB (http://www.interpeak.se). All rights reserved.'configuring 'iplite'configuring 'ipppp'starting 'iplite'starting 'ipppp'Configured bios support level=1:traffic
Turning off Gigabit Ethernet Tx Flow Control
dda/mpc834x/tsec0: Using mode '100fdx'
7.952 netw: Attaching eth0[2] (tsec0:0).
Turning off Gigabit Ethernet Tx Flow Control
dda/mpc834x/tsec1: Using mode '1000fdx'
8.052 netw: Attaching eth1[3] (tsec1:1).
8.053 netw: Bringing up eth0.
8.053 netw: Bringing up eth1.
8.053 netw: Creating network processes.
8.054 ifplugd: Process starting.
8.054 ifplugd: Add interface 'eth0'.
8.054 ifplugd: Monitoring 1 interfaces.
8.054 ifplugd: Linkstate on eth0 changed to Up.
8.054 ifplugd: Take action for linkup on eth0.
8.055 ifplugd: Bringing up eth0.
8.055 ifplugd: Add interface 'eth1'.
8.055 netw: Monitoring 2 interface(s).
8.055 netw: Network interface 'eth0' is up.
8.055 netw: Set hostname to "192.168.255.253".
8.055 netw: 1 / 2 IFs configured - 1 responses received.
8.055 netw: Maybe activating network due to IF_NOTIFY_UP for 'eth0' - is_activated = 0....
8.055 netw: Asking ymer for time.
8.055 netw: Failed to resolve 'ymer'.
8.055 netw: Failed to obtain time.
8.055 netw: Network activated -> reply startup signal....
8.056 netw: Network interface 'eth1' is up.
8.057 ifplugd: Monitoring 2 interfaces.
8.057 ifplugd: Linkstate on eth1 changed to Up.
8.057 ifplugd: Take action for linkup on eth1.
Turning off Gigabit Ethernet Tx Flow Control
dda/mpc834x/tsec1: Using mode '1000fdx'
8.157 netw: Set hostname to "192.168.2.5".
8.157 netw: 2 / 2 IFs configured - 2 responses received.
Starting TELNET server on port 23
Starting FTP server on port 21 startdir /
8.240 ifplugd: Bringing up eth1.
* Setting Date: 2016-08-03  UTC Time: 13:56:31
* Versions: 0,V04.56 2016-01-11 ;1,V01.00 2016-01-11 ;2,V03.01 2014-11-26 ;3,V04.06 2011-04-29 ;
Creating DMA Interrupt Handler processCreating DMA Interrupt Handler processPPSSynch @ Systemtime 25527088
PPSSynch kVco estimated: 0.054085
PPSSynch SynchState: 0
* Startup receiver complete
* createStaticClients:
Starting NVRAM client
* NVRAM:Init; DataSet Ok; Warm Boot
15.165 ifplugd: Linkstate on eth0 changed to Down.
* NVRAM:Init ready
NVRAM client started [r = 2]
* Starting RS232 client
RS232 client started [r = 3]
19.165 ifplugd: Linkstate on eth0 changed to Up.
420.165 ifplugd: Linkstate on eth0 changed to Down.
422.165 ifplugd: Linkstate on eth0 changed to Up.
2474.166 ifplugd: Linkstate on eth0 changed to Down.
2476.166 ifplugd: Linkstate on eth0 changed to Up.
2639.166 ifplugd: Linkstate on eth0 changed to Down.
2641.166 ifplugd: Linkstate on eth0 changed to Up.
2979.166 ifplugd: Linkstate on eth0 changed to Down.
2981.166 ifplugd: Linkstate on eth0 changed to Up.
eb500> 
``

    



