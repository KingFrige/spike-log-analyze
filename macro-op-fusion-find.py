#!/usr/bin/python3

import pandas as pd 
from matplotlib import pyplot as plt 
import argparse
import re
import os

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--path", type=str, default="0")
args = parser.parse_args()

path_base = os.path.basename(args.path) 
file_name = path_base.split('.')[0]

spike_log = open(args.path, "r")

def indexed_load(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'add' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- indexed load --------------')
    print()
  return find_flag

def indexed_effictive_load(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'slli' and line0_list[4] == 'add'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- indexed effictive load --------------')
    print()
  return find_flag

def threeInsn_indexed_effictive_load(lines, line_num):
  find_flag = 0
  line2_list = re.sub(r',','',lines[2]).split();
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd0_match = (line2_list[5] == line1_list[5]) and (line1_list[5] in line1_list[6:-1])
  rd1_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line2_list[4] == 'slli' and line1_list[4] == 'add' and line0_list[4] == 'ld'
  if(rd0_match and rd1_match and insn_match):
    find_flag = 1
    print(line_num-2, lines[2], end='')
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- threeInsn indexed effictive load --------------', end='\n')
    print()
  return find_flag

def clear_upper_word(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'slli' and line0_list[4] == 'srli'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- clear upper word --------------')
    print()
  return find_flag

def load_upper_imm_addi(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'lui' and line0_list[4] == 'addi'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- load upper imm addi --------------')
    print()
  return find_flag

def load_upper_imm_ld(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'lui' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- load upper imm ld --------------')
    print()
  return find_flag

def load_global_imm(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'auipc' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- load global imm --------------')
    print()
  return find_flag

def calc_target_addr(lines, line_num):
  pass
  
def signle32_zero_ext(lines, line_num):
  pass

def wide_mul(lines, line_num):
  pass

def wide_div(lines, line_num):
  pass

def load_pair(lines, line_num):
  find_flag = 0
  line1_list = re.sub(r',','',lines[1]).split();
  line0_list = re.sub(r',','',lines[0]).split();
  rs_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'ld' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print(line_num-1, lines[1], end='')
    print(line_num, lines[0], end='')
    print('------- load pair --------------')
    print()
  return find_flag

def post_indexed_load(lines, line_num):
  pass

find_cnt = 0
list_lines = ["", "", ""]
list_index = 0
macro_opFusion_num = 0
line_num = 0

indexed_load_cnt = 0
indexed_effictive_load_cnt = 0
clear_upper_word_cnt = 0
load_upper_imm_addi_cnt = 0
load_upper_imm_ld_cnt = 0
load_global_imm_cnt = 0
threeInsn_indexed_effictive_load_cnt = 0

for line in spike_log:
  line_list = re.sub(r',','',line).split();
  line_num  = line_num + 1
  if(len(line_list) > 5):
    list_lines[2] = list_lines[1]
    list_lines[1] = list_lines[0]
    list_lines[0] = line
  if(line_num > 1):
    indexed_load_cnt += indexed_load(list_lines, line_num)
    indexed_effictive_load_cnt += indexed_effictive_load(list_lines, line_num)
    clear_upper_word_cnt += clear_upper_word(list_lines, line_num)
    load_upper_imm_addi_cnt += load_upper_imm_addi(list_lines, line_num)
    load_upper_imm_ld_cnt += load_upper_imm_ld(list_lines, line_num)
    load_global_imm_cnt += load_global_imm(list_lines, line_num)

  if(line_num > 2):
    threeInsn_indexed_effictive_load_cnt += threeInsn_indexed_effictive_load(list_lines, line_num)

macro_opFusion_num = indexed_load_cnt + indexed_effictive_load_cnt + clear_upper_word_cnt + load_upper_imm_addi_cnt + load_upper_imm_ld_cnt + load_global_imm_cnt + threeInsn_indexed_effictive_load_cnt

op_fusion_ratio = macro_opFusion_num / line_num
print("Potential macro opFusion ", macro_opFusion_num)  
print("macro opFusion ratio : ", op_fusion_ratio)  
