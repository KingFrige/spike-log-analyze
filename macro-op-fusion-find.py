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

def print_lines_list(line_num, lines, annot_str, three_line = False):
  if(three_line):
    print(line_num-2, ' '.join(lines[2]))
  print(line_num-1,   ' '.join(lines[1]))
  print(line_num,     ' '.join(lines[0]))
  print('------- %s --------------', annot_str)
  print()

def indexed_load(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'add' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "indexed load")
  return find_flag

def indexed_effictive_load(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'slli' and line0_list[4] == 'add'
  if(rd_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "indexed effictive load")
  return find_flag

def threeInsn_indexed_effictive_load(lines, line_num):
  find_flag = 0
  line2_list = lines[2]
  line1_list = lines[1]
  line0_list = lines[0]
  rd0_match = (line2_list[5] == line1_list[5]) and (line1_list[5] in line1_list[6:-1])
  rd1_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line2_list[4] == 'slli' and line1_list[4] == 'add' and line0_list[4] == 'ld'
  if(rd0_match and rd1_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "threeInsn indexed effictive load", True)
  return find_flag

def clear_upper_word(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'slli' and line0_list[4] == 'srli'
  if(rd_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "clear upper word")
  return find_flag

def load_upper_imm_addi(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'lui' and line0_list[4] == 'addi'
  if(rd_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "load upper imm addi")
  return find_flag

def load_upper_imm_ld(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'lui' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "load upper imm ld")
  return find_flag

def load_global_imm(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  rd_match = (line1_list[5] == line0_list[5]) and (line0_list[5] in line0_list[6:-1])
  insn_match = line1_list[4] == 'auipc' and line0_list[4] == 'ld'
  if(rd_match and insn_match):
    find_flag = 1
    print_lines_list(line_num, lines, "load global imm")
  return find_flag

def calc_target_addr(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  if(len(line0_list) > 6 and len(line1_list) > 6):
    rd_match = line0_list[5] in line0_list[6]
    insn_match = line1_list[4] == 'auipc' and line0_list[4] == 'jalr'
    if(rd_match and insn_match):
      find_flag = 1
      print_lines_list(line_num, lines, "Fused far jump and link with calculated target address")
  return find_flag
  
def signle32_zero_ext(lines, line_num):
  pass

def wide_mul(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  if(len(line0_list) > 7 and len(line1_list) > 7):
    rd_match = (line1_list[6] == line0_list[6]) and (line1_list[7] == line0_list[7])
    insn_match = 'mulh' in line1_list[4] and line0_list[4] == 'mul'
    if(rd_match and insn_match):
      find_flag = 1
      print_lines_list(line_num, lines, "wide multiply")
  return find_flag

def wide_div(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  if(len(line0_list) > 7 and len(line1_list) > 7):
    rd_match = (line1_list[6] == line0_list[6]) and (line1_list[7] == line0_list[7])
    insn_match = 'div' in line1_list[4] and 'rem' in line0_list[4]
    if(rd_match and insn_match):
      find_flag = 1
      print_lines_list(line_num, lines, "wide divide & remainder")
  return find_flag

def load_pair(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  if(len(line0_list) > 6 and len(line1_list) > 6):
    pattern = r'[(](.*?)[)]'
    line1_rs = re.findall(pattern, line1_list[6])
    line0_rs = re.findall(pattern, line0_list[6])
    rs_match = len(line1_rs) and len(line0_rs) and line1_rs[0] == line0_rs[0]
    insn_match = line1_list[4] == 'ld' and line0_list[4] == 'ld'
    if(rs_match and insn_match):
      find_flag = 1
      print_lines_list(line_num, lines, "load pair")
  return find_flag

def post_indexed_load(lines, line_num):
  find_flag = 0
  line1_list = lines[1]
  line0_list = lines[0]
  if(len(line0_list) > 7 and len(line1_list) > 6):
    pattern = r'[(](.*?)[)]'
    line1_rs = re.findall(pattern, line1_list[6])
    line0_rd = line0_list[6]
    line0_rs = line0_list[7]
    rs_match = len(line1_rs) and line1_rs[0] == line0_rs and line0_rs == line0_rd
    insn_match = line1_list[4] == 'ld' and line0_list[4] == 'add'
    if(rs_match and insn_match):
      find_flag = 1
      print_lines_list(line_num, lines, "post indexed load")
  return find_flag



def main():
  find_cnt = 0
  lines_list = ["", "", ""]
  list_index = 0
  macro_opFusion_num = 0
  line_num = 0
  
  indexed_load_cnt = 0
  indexed_effictive_load_cnt = 0
  clear_upper_word_cnt = 0
  load_upper_imm_addi_cnt = 0
  load_upper_imm_ld_cnt = 0
  load_global_imm_cnt = 0
  calc_target_addr_cnt = 0
  threeInsn_indexed_effictive_load_cnt = 0
  wide_mul_cnt = 0
  wide_div_cnt = 0
  load_pair_cnt = 0
  post_indexed_load_cnt = 0
  
  for line in spike_log:
    line_list = re.sub(r',','',line).split();
    line_num  = line_num + 1
    if(len(line_list) > 5):
      lines_list[2] = lines_list[1]
      lines_list[1] = lines_list[0]
      lines_list[0] = line_list
    if(line_num > 1):
      indexed_load_cnt += indexed_load(lines_list, line_num)
      indexed_effictive_load_cnt += indexed_effictive_load(lines_list, line_num)
      clear_upper_word_cnt += clear_upper_word(lines_list, line_num)
      load_upper_imm_addi_cnt += load_upper_imm_addi(lines_list, line_num)
      load_upper_imm_ld_cnt += load_upper_imm_ld(lines_list, line_num)
      load_global_imm_cnt += load_global_imm(lines_list, line_num)
      calc_target_addr_cnt += calc_target_addr(lines_list, line_num)
      wide_mul_cnt += wide_mul(lines_list, line_num)
      wide_div_cnt += wide_div(lines_list, line_num)
      load_pair_cnt += load_pair(lines_list, line_num)
      post_indexed_load_cnt += post_indexed_load(lines_list, line_num)
  
    if(line_num > 2):
      threeInsn_indexed_effictive_load_cnt += threeInsn_indexed_effictive_load(lines_list, line_num)
  
  macro_opFusion_num = indexed_load_cnt + indexed_effictive_load_cnt + clear_upper_word_cnt + load_upper_imm_addi_cnt + load_upper_imm_ld_cnt + load_global_imm_cnt + calc_target_addr_cnt + threeInsn_indexed_effictive_load_cnt + wide_mul_cnt + wide_div_cnt + load_pair_cnt + post_indexed_load_cnt
  
  op_fusion_ratio = macro_opFusion_num / line_num
  print("Potential macro opFusion ", macro_opFusion_num)  
  print("macro opFusion ratio : ", op_fusion_ratio)  

if __name__ == '__main__':
  main()


