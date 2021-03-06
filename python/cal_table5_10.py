#!/usr/bin/env python
"""
Calculate table 5 and table 10
"""

__author__ = "XIAO Suyu <xiaosuyu@ihep.ac.cn>"
__copyright__ = "Copyright (c) XIAO Suyu"
__created__ = "[2018-02-01 Thu 17:21]"

import math

n_anything = 57795500.0
n_anything_err = 8874.0
#n_anything = 18658100.0
#n_anything_err = 5000
n_anything_09 = 18658100.0

n_invisible = 397611.0
n_invisible_err = 684.0
n_invisible_09 = 137770.0

n_other = 16163.0
n_other_09 = 3877.0

n_total_2B_09 = 134586.0
N_invisible_09 = -670.0

b_mumu = 5.961
b_ee = 5.971
b_nn = 0.209
b_pp = 0.202
b_mumu_err = 0.033
b_ee_err = 0.032
b_nn_err = 0.016
b_pp_err = 0.0029

eff_mumu = 6.24
eff_ee = 6.32
eff_nn = 6.13
eff_pp = 2.64
#eff_mumu = 5.93
#eff_ee = 5.93
#eff_nn = 6.09
#eff_pp = 2.54
eff_2b_err = 0.02

eff_trigger = 99.4
eff_trigger_err = 0.1

n_mumu_09 = 65558.0
n_ee_09 = 65668.0
n_nn_09 = 2361.0
n_pp_09 = 999.0

stat_err = 0.03
fit_err = 0.44
n_gam_err = 1.90
trig_err = 0.12
mumu_shower_err = 0.5
ee_shower_err = 0.6
nn_shower_err = 41.5
pp_shower_err = 1.3

print "\nPsip_data_12/09 \t= \t%.4f" % (341.0/106.0)

print "\nn_anything \t= \t%d +- %d" % (n_anything, n_anything_err), "\tratio_12/09 = %.3f" % (n_anything / n_anything_09)
print "n_invisible \t= \t%d +- %d" % (n_invisible, n_invisible_err), "\t\tratio_12/09 = %.3f" % (n_invisible / n_invisible_09)
print "n_other \t= \t%d" % n_other, "\t\t\tratio_12/09 = %.3f" % (n_other / n_other_09)
print "eff_nunu = %.6f" % (196596.0/500000)

n_mumu = n_anything * b_mumu * eff_mumu * eff_trigger / 1000000
n_ee = n_anything * b_ee * eff_ee * eff_trigger / 1000000
n_nn = n_anything * b_nn * eff_nn * eff_trigger / 1000000
n_pp = n_anything * b_pp * eff_pp * eff_trigger / 1000000
n_mumu_err = n_mumu * math.sqrt( (b_mumu_err/b_mumu)**2 + (eff_2b_err/eff_mumu)**2 + stat_err**2 + fit_err**2 + n_gam_err**2 + trig_err**2 + mumu_shower_err**2 )/100
n_ee_err = n_ee * math.sqrt( (b_ee_err/b_ee)**2 + (eff_2b_err/eff_ee)**2 + stat_err**2 + fit_err**2 + n_gam_err**2 + trig_err**2 + ee_shower_err**2 )/100
n_nn_err = n_nn * math.sqrt( (b_nn_err/b_nn)**2 + (eff_2b_err/eff_nn)**2 + stat_err**2 + fit_err**2 + n_gam_err**2 + trig_err**2 + nn_shower_err**2 )/100
n_pp_err = n_pp * math.sqrt( (b_pp_err/b_pp)**2 + (eff_2b_err/eff_pp)**2 + stat_err**2 + fit_err**2 + n_gam_err**2 + trig_err**2 + pp_shower_err**2 )/100

print "\nstat_err \t= \t", stat_err
print "fit_err \t= \t", fit_err
print "n_gam_err \t= \t", n_gam_err
print "trig_err \t= \t", trig_err
print "\t\t\tmumu\tee\tnn\tpp"
print "BF_err \t\t= \t%.3f \t%.3f \t%.3f \t%.3f" %(b_mumu_err/b_mumu*100, b_ee_err/b_ee*100, b_nn_err/b_nn*100, b_pp_err/b_pp*100)
print "MC_err \t\t= \t%.3f \t%.3f \t%.3f \t%.3f" %(eff_2b_err/eff_mumu*100, eff_2b_err/eff_ee*100, eff_2b_err/eff_nn*100, eff_2b_err/eff_pp*100)
print "shower_err \t= \t%.1f \t%.1f \t%.1f \t%.1f" %(mumu_shower_err, ee_shower_err, nn_shower_err, pp_shower_err)

print "\nItems",      "\t\tBF(%)", "\t\teff_2B(%)", "\teff_trig(%)", "\tNumber", "\t\t\tNumber_09", "\tratio_12/09"
print "jpsi->mumu", "\t%.3f+-%.3f"%(b_mumu, b_mumu_err), "\t%.2f+-%.2f"%(eff_mumu, eff_2b_err), "\t%.1f+-%.1f"%(eff_trigger, eff_trigger_err), "\t%.2f+-%.2f"%(n_mumu, n_mumu_err), "\t%d"%n_mumu_09, "\t\t%.3f"%(n_mumu/n_mumu_09)
print "jpsi->ee", "\t%.3f+-%.3f"%(b_ee, b_ee_err), "\t%.2f+-%.2f"%(eff_ee, eff_2b_err), "\t%.1f+-%.1f"%(eff_trigger, eff_trigger_err), "\t%.2f+-%.2f"%(n_ee, n_ee_err), "\t%d"%n_ee_09, "\t\t%.3f"%(n_ee/n_ee_09)
print "jpsi->nn", "\t%.3f+-%.3f"%(b_nn, b_nn_err), "\t%.2f+-%.2f"%(eff_nn, eff_2b_err), "\t%.1f+-%.1f"%(eff_trigger, eff_trigger_err), "\t%.2f+-%.2f"%(n_nn, n_nn_err), "\t%d"%n_nn_09, "\t\t%.3f"%(n_nn/n_nn_09)
print "jpsi->pp", "\t%.3f+-%.3f"%(b_pp, b_pp_err), "\t%.2f+-%.2f"%(eff_pp, eff_2b_err), "\t%.1f+-%.1f"%(eff_trigger, eff_trigger_err), "\t%.2f+-%.2f"%(n_pp, n_pp_err), "\t\t%d"%n_pp_09, "\t\t%.3f"%(n_pp/n_pp_09)

n_total_2B = n_mumu + n_ee + n_nn + n_pp
n_total_2B_err = math.sqrt((n_mumu + n_ee + n_nn + n_pp)**2 * (stat_err**2 + fit_err**2 + n_gam_err**2 + trig_err**2) + n_mumu**2 * ((b_mumu_err/b_mumu)**2 + (eff_2b_err/eff_mumu)**2 + mumu_shower_err**2) + n_ee**2 * ((b_ee_err/b_ee)**2 + (eff_2b_err/eff_ee)**2 + ee_shower_err**2) + n_nn**2 * ((b_nn_err/b_nn)**2 + (eff_2b_err/eff_nn)**2 + nn_shower_err**2) + n_pp**2 * ((b_pp_err/b_pp)**2 + (eff_2b_err/eff_pp)**2 + pp_shower_err**2) ) /100
#n_total_2B_err = math.sqrt((134586)**2 * (stat_err**2 + fit_err*2 + n_gam_err**2 + trig_err**2) + 65558**2 * ((0.55)**2 + (0.33)**2 + mumu_shower_err**2) + 65668**2 * ((0.54)**2 + (0.33)**2 + ee_shower_err**2) + 2361**2 * ((7.66)**2 + (0.40)**2 + nn_shower_err**2) + 999**2 * ((1.37)**2 + (0.62)**2 + pp_shower_err**2) )
print "\nn_total_2B/n_anything = %f" % (n_total_2B/n_anything), "\tn_total_2B_09/n_anything_09 = %f" % (n_total_2B_09/n_anything_09)
print "\nn_total_2B \t= %.2f+-%.2f" % (n_total_2B, n_total_2B_err), "\tratio_12/09 \t= %.6f" % (n_total_2B/n_total_2B_09)
#print "n_total_peaking = %.2f" % (n_mumu + n_ee + n_nn + n_pp + n_other)
N_invisible = n_invisible - n_total_2B - n_other * eff_trigger / 100
print "N_invisible \t= %.2f" % N_invisible, "\t\tratio_12/09 \t= %f" % (N_invisible / N_invisible_09)
#a = 3.0
#b = 5
#print "test = %f" % math.sqrt(b/a)

print "\n"
