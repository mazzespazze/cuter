#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json, datetime
import cuter_global as cglb

DATA_RECEIVED_LOG = "data_received.log"
JSON_LOADED_LOG = "json_loaded.log"
MODEL_UNKNOWN = "model_unknown.log"
DEBUG_LOG = "debug.log"


def debug_info(data):
  if cglb.__LOG_DEBUG_INFO__:
    fd = open(DEBUG_LOG, "a")
    fd.write("{}\n".format(data))
    fd.flush()
    fd.close()

def data_received(data):
  if cglb.__LOG_DATA_RECEIVED__:
    fd = open(DATA_RECEIVED_LOG, "a")
    fd.write("{}\n".format(data))
    fd.flush()
    fd.close()

def json_loaded(i, k, opcode, tag, json_data, rev):
  if cglb.__LOG_JSON_LOADED__:
    fd = open(JSON_LOADED_LOG, "a")
    fd.write("{}.\n".format(i))
    fd.write("  OPCODE {}\n".format(opcode))
    fd.write("  KIND {}\n".format(k))
    fd.write("  TAG {}\n".format(tag))
    fd.write("  JSON {}\n".format(json_data))
    fd.write("  REVERSIBLE {}\n".format(rev))
    fd.flush()
    fd.close()

def model_unknown(quantifier_axs, axs):
  if cglb.__LOG_MODEL_UNKNOWN__:
    fd = open(MODEL_UNKNOWN, "a")
    fd.write("{}\n".format(datetime.datetime.now()))
    fd.write("  QAXS {}\n".format(quantifier_axs))
    fd.write("  AXS {}\n".format(axs))
    fd.flush()
    fd.close()

def clean_empty_logs():
  clean_empty_log(DATA_RECEIVED_LOG)
  clean_empty_log(JSON_LOADED_LOG)
  clean_empty_log(MODEL_UNKNOWN)

def clean_empty_log(log):
  try:
    if os.stat(log).st_size == 0:
      os.remove(log)
  except:
    pass