# coding=utf-8
import re

edcut =[
  {
    "result": "财务报表",
    "pageId": 1
  },
  {
    "result": "财务报表",
    "pageId": 2
  },
  {
    "result": "财务报表",
    "pageId": 3
  },
  {
    "result": "财务报表",
    "pageId": 4
  },
  {
    "result": "财务报表",
    "pageId": 5
  }
]

ocr_res =[
  {
    "page_id": 1,
    "type": "text",
    "range": {
      "left": 549.9107358333513,
      "right": 705.7065662080411,
      "top": 72.6676014497784,
      "bottom": 105.10620800444936,
      "center_x": 627.8086510206962,
      "center_y": 88.88690472711389
    },
    "text": "资产负债表"
  },
  {
    "page_id": 1,
    "type": "text",
    "range": {
      "left": 118.65317630767822,
      "right": 226.28206210035253,
      "top": 1565.916404339035,
      "bottom": 1586.0376019194946,
      "center_x": 172.46761920401536,
      "center_y": 1575.9770031292646
    },
    "text": "单位负责人："
  },
  {
    "page_id": 1,
    "type": "text",
    "range": {
      "left": 461.3152484893799,
      "right": 569.0107920101449,
      "top": 1566.5786105809368,
      "bottom": 1586.579830862931,
      "center_x": 515.1630202497624,
      "center_y": 1576.5792207219338
    },
    "text": "会计负责人："
  },
  {
    "page_id": 1,
    "type": "text",
    "range": {
      "left": 803.526862620051,
      "right": 875.8232910633087,
      "top": 1567.2676999157425,
      "bottom": 1586.9677197763995,
      "center_x": 839.6750768416798,
      "center_y": 1577.117709846071
    },
    "text": "制表人 1"
  },
  {
    "page_id": 1,
    "type": "table",
    "cells": [
      {
        "left": 115,
        "right": 883,
        "top": 126,
        "bottom": 152,
        "center_x": 499.0,
        "center_y": 139.0,
        "text": "编制单位：苏州梅克兰循环科技有限公司 2022-12-31"
      },
      {
        "left": 115,
        "right": 271,
        "top": 152,
        "bottom": 185,
        "center_x": 193.0,
        "center_y": 168.5,
        "text": "资产"
      },
      {
        "left": 115,
        "right": 271,
        "top": 185,
        "bottom": 217,
        "center_x": 193.0,
        "center_y": 201.0,
        "text": "流动资产："
      },
      {
        "left": 115,
        "right": 271,
        "top": 217,
        "bottom": 250,
        "center_x": 193.0,
        "center_y": 233.5,
        "text": "货币资金"
      },
      {
        "left": 115,
        "right": 271,
        "top": 250,
        "bottom": 284,
        "center_x": 193.0,
        "center_y": 267.0,
        "text": "交易性金融资产"
      },
      {
        "left": 115,
        "right": 271,
        "top": 284,
        "bottom": 318,
        "center_x": 193.0,
        "center_y": 301.0,
        "text": "衍生金融资产"
      },
      {
        "left": 271,
        "right": 328,
        "top": 152,
        "bottom": 185,
        "center_x": 299.5,
        "center_y": 168.5,
        "text": "行次"
      },
      {
        "left": 115,
        "right": 271,
        "top": 318,
        "bottom": 351,
        "center_x": 193.0,
        "center_y": 334.5,
        "text": "应收票据"
      },
      {
        "left": 271,
        "right": 328,
        "top": 185,
        "bottom": 217,
        "center_x": 299.5,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 351,
        "bottom": 385,
        "center_x": 193.0,
        "center_y": 368.0,
        "text": "应收账款"
      },
      {
        "left": 328,
        "right": 471,
        "top": 152,
        "bottom": 185,
        "center_x": 399.5,
        "center_y": 168.5,
        "text": "年初余额"
      },
      {
        "left": 271,
        "right": 328,
        "top": 217,
        "bottom": 250,
        "center_x": 299.5,
        "center_y": 233.5,
        "text": "1"
      },
      {
        "left": 115,
        "right": 271,
        "top": 385,
        "bottom": 418,
        "center_x": 193.0,
        "center_y": 401.5,
        "text": "应收款项融资"
      },
      {
        "left": 328,
        "right": 471,
        "top": 185,
        "bottom": 217,
        "center_x": 399.5,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 250,
        "bottom": 284,
        "center_x": 299.5,
        "center_y": 267.0,
        "text": "2"
      },
      {
        "left": 115,
        "right": 271,
        "top": 418,
        "bottom": 452,
        "center_x": 193.0,
        "center_y": 435.0,
        "text": "预付款项"
      },
      {
        "left": 328,
        "right": 471,
        "top": 217,
        "bottom": 250,
        "center_x": 399.5,
        "center_y": 233.5,
        "text": "21,627,911.73"
      },
      {
        "left": 271,
        "right": 328,
        "top": 284,
        "bottom": 318,
        "center_x": 299.5,
        "center_y": 301.0,
        "text": "3"
      },
      {
        "left": 115,
        "right": 271,
        "top": 452,
        "bottom": 484,
        "center_x": 193.0,
        "center_y": 468.0,
        "text": "其他应收款"
      },
      {
        "left": 328,
        "right": 471,
        "top": 250,
        "bottom": 284,
        "center_x": 399.5,
        "center_y": 267.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 318,
        "bottom": 351,
        "center_x": 299.5,
        "center_y": 334.5,
        "text": "4"
      },
      {
        "left": 115,
        "right": 271,
        "top": 484,
        "bottom": 518,
        "center_x": 193.0,
        "center_y": 501.0,
        "text": "存货"
      },
      {
        "left": 328,
        "right": 471,
        "top": 284,
        "bottom": 318,
        "center_x": 399.5,
        "center_y": 301.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 351,
        "bottom": 385,
        "center_x": 299.5,
        "center_y": 368.0,
        "text": "5"
      },
      {
        "left": 471,
        "right": 614,
        "top": 152,
        "bottom": 185,
        "center_x": 542.5,
        "center_y": 168.5,
        "text": "期末余额"
      },
      {
        "left": 115,
        "right": 271,
        "top": 518,
        "bottom": 552,
        "center_x": 193.0,
        "center_y": 535.0,
        "text": "合同资产"
      },
      {
        "left": 328,
        "right": 471,
        "top": 318,
        "bottom": 351,
        "center_x": 399.5,
        "center_y": 334.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 185,
        "bottom": 217,
        "center_x": 542.5,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 385,
        "bottom": 418,
        "center_x": 299.5,
        "center_y": 401.5,
        "text": "6"
      },
      {
        "left": 115,
        "right": 271,
        "top": 552,
        "bottom": 586,
        "center_x": 193.0,
        "center_y": 569.0,
        "text": "持有待售资产"
      },
      {
        "left": 328,
        "right": 471,
        "top": 351,
        "bottom": 385,
        "center_x": 399.5,
        "center_y": 368.0,
        "text": "26,330,584.17"
      },
      {
        "left": 471,
        "right": 614,
        "top": 217,
        "bottom": 250,
        "center_x": 542.5,
        "center_y": 233.5,
        "text": "15,709,953.27"
      },
      {
        "left": 271,
        "right": 328,
        "top": 418,
        "bottom": 452,
        "center_x": 299.5,
        "center_y": 435.0,
        "text": "7"
      },
      {
        "left": 115,
        "right": 271,
        "top": 586,
        "bottom": 618,
        "center_x": 193.0,
        "center_y": 602.0,
        "text": "一年内到期的非流动资产"
      },
      {
        "left": 328,
        "right": 471,
        "top": 385,
        "bottom": 418,
        "center_x": 399.5,
        "center_y": 401.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 250,
        "bottom": 284,
        "center_x": 542.5,
        "center_y": 267.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 452,
        "bottom": 484,
        "center_x": 299.5,
        "center_y": 468.0,
        "text": "8"
      },
      {
        "left": 115,
        "right": 271,
        "top": 618,
        "bottom": 652,
        "center_x": 193.0,
        "center_y": 635.0,
        "text": "其他流动资产"
      },
      {
        "left": 328,
        "right": 471,
        "top": 418,
        "bottom": 452,
        "center_x": 399.5,
        "center_y": 435.0,
        "text": "21,812,565.11"
      },
      {
        "left": 471,
        "right": 614,
        "top": 284,
        "bottom": 318,
        "center_x": 542.5,
        "center_y": 301.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 484,
        "bottom": 518,
        "center_x": 299.5,
        "center_y": 501.0,
        "text": "9"
      },
      {
        "left": 614,
        "right": 799,
        "top": 152,
        "bottom": 185,
        "center_x": 706.5,
        "center_y": 168.5,
        "text": "负债和所有者权益"
      },
      {
        "left": 115,
        "right": 271,
        "top": 652,
        "bottom": 685,
        "center_x": 193.0,
        "center_y": 668.5,
        "text": "流动资产合计"
      },
      {
        "left": 328,
        "right": 471,
        "top": 452,
        "bottom": 484,
        "center_x": 399.5,
        "center_y": 468.0,
        "text": "1,127,499.00"
      },
      {
        "left": 471,
        "right": 614,
        "top": 318,
        "bottom": 351,
        "center_x": 542.5,
        "center_y": 334.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 518,
        "bottom": 552,
        "center_x": 299.5,
        "center_y": 535.0,
        "text": "10"
      },
      {
        "left": 614,
        "right": 799,
        "top": 185,
        "bottom": 217,
        "center_x": 706.5,
        "center_y": 201.0,
        "text": "流动负债："
      },
      {
        "left": 115,
        "right": 271,
        "top": 685,
        "bottom": 718,
        "center_x": 193.0,
        "center_y": 701.5,
        "text": "非流动资产："
      },
      {
        "left": 328,
        "right": 471,
        "top": 484,
        "bottom": 518,
        "center_x": 399.5,
        "center_y": 501.0,
        "text": "5,377,878.14"
      },
      {
        "left": 471,
        "right": 614,
        "top": 351,
        "bottom": 385,
        "center_x": 542.5,
        "center_y": 368.0,
        "text": "33,701,842.62"
      },
      {
        "left": 271,
        "right": 328,
        "top": 552,
        "bottom": 586,
        "center_x": 299.5,
        "center_y": 569.0,
        "text": "11"
      },
      {
        "left": 614,
        "right": 799,
        "top": 217,
        "bottom": 250,
        "center_x": 706.5,
        "center_y": 233.5,
        "text": "短期借款"
      },
      {
        "left": 115,
        "right": 271,
        "top": 718,
        "bottom": 752,
        "center_x": 193.0,
        "center_y": 735.0,
        "text": "债权投资"
      },
      {
        "left": 328,
        "right": 471,
        "top": 518,
        "bottom": 552,
        "center_x": 399.5,
        "center_y": 535.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 385,
        "bottom": 418,
        "center_x": 542.5,
        "center_y": 401.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 586,
        "bottom": 618,
        "center_x": 299.5,
        "center_y": 602.0,
        "text": "12"
      },
      {
        "left": 614,
        "right": 799,
        "top": 250,
        "bottom": 284,
        "center_x": 706.5,
        "center_y": 267.0,
        "text": "交易性金融负债7"
      },
      {
        "left": 115,
        "right": 271,
        "top": 752,
        "bottom": 786,
        "center_x": 193.0,
        "center_y": 769.0,
        "text": "其他债权投资"
      },
      {
        "left": 328,
        "right": 471,
        "top": 552,
        "bottom": 586,
        "center_x": 399.5,
        "center_y": 569.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 418,
        "bottom": 452,
        "center_x": 542.5,
        "center_y": 435.0,
        "text": "2,038,269.74"
      },
      {
        "left": 271,
        "right": 328,
        "top": 618,
        "bottom": 652,
        "center_x": 299.5,
        "center_y": 635.0,
        "text": "13"
      },
      {
        "left": 614,
        "right": 799,
        "top": 284,
        "bottom": 318,
        "center_x": 706.5,
        "center_y": 301.0,
        "text": "衍生金融负债"
      },
      {
        "left": 115,
        "right": 271,
        "top": 786,
        "bottom": 820,
        "center_x": 193.0,
        "center_y": 803.0,
        "text": "长期应收款"
      },
      {
        "left": 328,
        "right": 471,
        "top": 586,
        "bottom": 618,
        "center_x": 399.5,
        "center_y": 602.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 452,
        "bottom": 484,
        "center_x": 542.5,
        "center_y": 468.0,
        "text": "1,036,020.00"
      },
      {
        "left": 271,
        "right": 328,
        "top": 652,
        "bottom": 685,
        "center_x": 299.5,
        "center_y": 668.5,
        "text": "14"
      },
      {
        "left": 614,
        "right": 799,
        "top": 318,
        "bottom": 351,
        "center_x": 706.5,
        "center_y": 334.5,
        "text": "应付票据"
      },
      {
        "left": 115,
        "right": 271,
        "top": 820,
        "bottom": 852,
        "center_x": 193.0,
        "center_y": 836.0,
        "text": "长期股权投资"
      },
      {
        "left": 328,
        "right": 471,
        "top": 618,
        "bottom": 652,
        "center_x": 399.5,
        "center_y": 635.0,
        "text": "623,731.95"
      },
      {
        "left": 799,
        "right": 856,
        "top": 152,
        "bottom": 185,
        "center_x": 827.5,
        "center_y": 168.5,
        "text": "行次"
      },
      {
        "left": 471,
        "right": 614,
        "top": 484,
        "bottom": 518,
        "center_x": 542.5,
        "center_y": 501.0,
        "text": "6,802,676.05"
      },
      {
        "left": 271,
        "right": 328,
        "top": 685,
        "bottom": 718,
        "center_x": 299.5,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 351,
        "bottom": 385,
        "center_x": 706.5,
        "center_y": 368.0,
        "text": "应付账款"
      },
      {
        "left": 115,
        "right": 271,
        "top": 852,
        "bottom": 886,
        "center_x": 193.0,
        "center_y": 869.0,
        "text": "其他权益工具投资"
      },
      {
        "left": 328,
        "right": 471,
        "top": 652,
        "bottom": 685,
        "center_x": 399.5,
        "center_y": 668.5,
        "text": "76,900,170.10"
      },
      {
        "left": 799,
        "right": 856,
        "top": 185,
        "bottom": 217,
        "center_x": 827.5,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 518,
        "bottom": 552,
        "center_x": 542.5,
        "center_y": 535.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 718,
        "bottom": 752,
        "center_x": 299.5,
        "center_y": 735.0,
        "text": "15"
      },
      {
        "left": 614,
        "right": 799,
        "top": 385,
        "bottom": 418,
        "center_x": 706.5,
        "center_y": 401.5,
        "text": "预收款项"
      },
      {
        "left": 115,
        "right": 271,
        "top": 886,
        "bottom": 919,
        "center_x": 193.0,
        "center_y": 902.5,
        "text": "其他非流动金融资产"
      },
      {
        "left": 883,
        "right": 937,
        "top": 126,
        "bottom": 152,
        "center_x": 910.0,
        "center_y": 139.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 152,
        "bottom": 185,
        "center_x": 869.5,
        "center_y": 168.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 685,
        "bottom": 718,
        "center_x": 399.5,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 217,
        "bottom": 250,
        "center_x": 827.5,
        "center_y": 233.5,
        "text": "35"
      },
      {
        "left": 471,
        "right": 614,
        "top": 552,
        "bottom": 586,
        "center_x": 542.5,
        "center_y": 569.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 752,
        "bottom": 786,
        "center_x": 299.5,
        "center_y": 769.0,
        "text": "16"
      },
      {
        "left": 614,
        "right": 799,
        "top": 418,
        "bottom": 452,
        "center_x": 706.5,
        "center_y": 435.0,
        "text": "合同负债"
      },
      {
        "left": 115,
        "right": 271,
        "top": 919,
        "bottom": 952,
        "center_x": 193.0,
        "center_y": 935.5,
        "text": "投资性房地产"
      },
      {
        "left": 883,
        "right": 937,
        "top": 152,
        "bottom": 185,
        "center_x": 910.0,
        "center_y": 168.5,
        "text": "年初"
      },
      {
        "left": 856,
        "right": 883,
        "top": 185,
        "bottom": 217,
        "center_x": 869.5,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 718,
        "bottom": 752,
        "center_x": 399.5,
        "center_y": 735.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 250,
        "bottom": 284,
        "center_x": 827.5,
        "center_y": 267.0,
        "text": "36"
      },
      {
        "left": 471,
        "right": 614,
        "top": 586,
        "bottom": 618,
        "center_x": 542.5,
        "center_y": 602.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 786,
        "bottom": 820,
        "center_x": 299.5,
        "center_y": 803.0,
        "text": "17"
      },
      {
        "left": 937,
        "right": 1142,
        "top": 126,
        "bottom": 152,
        "center_x": 1039.5,
        "center_y": 139.0,
        "text": "单位：元"
      },
      {
        "left": 614,
        "right": 799,
        "top": 452,
        "bottom": 484,
        "center_x": 706.5,
        "center_y": 468.0,
        "text": "应付职工薪酬"
      },
      {
        "left": 115,
        "right": 271,
        "top": 952,
        "bottom": 986,
        "center_x": 193.0,
        "center_y": 969.0,
        "text": "固定资产"
      },
      {
        "left": 883,
        "right": 937,
        "top": 185,
        "bottom": 217,
        "center_x": 910.0,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 217,
        "bottom": 250,
        "center_x": 869.5,
        "center_y": 233.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 752,
        "bottom": 786,
        "center_x": 399.5,
        "center_y": 769.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 284,
        "bottom": 318,
        "center_x": 827.5,
        "center_y": 301.0,
        "text": "37"
      },
      {
        "left": 937,
        "right": 999,
        "top": 152,
        "bottom": 185,
        "center_x": 968.0,
        "center_y": 168.5,
        "text": "余额"
      },
      {
        "left": 471,
        "right": 614,
        "top": 618,
        "bottom": 652,
        "center_x": 542.5,
        "center_y": 635.0,
        "text": "-252,400.91"
      },
      {
        "left": 271,
        "right": 328,
        "top": 820,
        "bottom": 852,
        "center_x": 299.5,
        "center_y": 836.0,
        "text": "18"
      },
      {
        "left": 614,
        "right": 799,
        "top": 484,
        "bottom": 518,
        "center_x": 706.5,
        "center_y": 501.0,
        "text": "应交税费"
      },
      {
        "left": 883,
        "right": 937,
        "top": 217,
        "bottom": 250,
        "center_x": 910.0,
        "center_y": 233.5,
        "text": "24,90"
      },
      {
        "left": 115,
        "right": 271,
        "top": 986,
        "bottom": 1020,
        "center_x": 193.0,
        "center_y": 1003.0,
        "text": "在建工程"
      },
      {
        "left": 856,
        "right": 883,
        "top": 250,
        "bottom": 284,
        "center_x": 869.5,
        "center_y": 267.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 786,
        "bottom": 820,
        "center_x": 399.5,
        "center_y": 803.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 318,
        "bottom": 351,
        "center_x": 827.5,
        "center_y": 334.5,
        "text": "38"
      },
      {
        "left": 937,
        "right": 999,
        "top": 185,
        "bottom": 217,
        "center_x": 968.0,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 652,
        "bottom": 685,
        "center_x": 542.5,
        "center_y": 668.5,
        "text": "59,036,360.77"
      },
      {
        "left": 271,
        "right": 328,
        "top": 852,
        "bottom": 886,
        "center_x": 299.5,
        "center_y": 869.0,
        "text": "19"
      },
      {
        "left": 614,
        "right": 799,
        "top": 518,
        "bottom": 552,
        "center_x": 706.5,
        "center_y": 535.0,
        "text": "其他应付款"
      },
      {
        "left": 883,
        "right": 937,
        "top": 250,
        "bottom": 284,
        "center_x": 910.0,
        "center_y": 267.0,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 1020,
        "bottom": 1054,
        "center_x": 193.0,
        "center_y": 1037.0,
        "text": "生产性生物资产"
      },
      {
        "left": 856,
        "right": 883,
        "top": 284,
        "bottom": 318,
        "center_x": 869.5,
        "center_y": 301.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 820,
        "bottom": 852,
        "center_x": 399.5,
        "center_y": 836.0,
        "text": "2,482,332.41"
      },
      {
        "left": 799,
        "right": 856,
        "top": 351,
        "bottom": 385,
        "center_x": 827.5,
        "center_y": 368.0,
        "text": "39"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 152,
        "bottom": 185,
        "center_x": 1070.5,
        "center_y": 168.5,
        "text": "期末余额"
      },
      {
        "left": 937,
        "right": 999,
        "top": 217,
        "bottom": 250,
        "center_x": 968.0,
        "center_y": 233.5,
        "text": "0,000.00"
      },
      {
        "left": 471,
        "right": 614,
        "top": 685,
        "bottom": 718,
        "center_x": 542.5,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 886,
        "bottom": 919,
        "center_x": 299.5,
        "center_y": 902.5,
        "text": "20"
      },
      {
        "left": 614,
        "right": 799,
        "top": 552,
        "bottom": 586,
        "center_x": 706.5,
        "center_y": 569.0,
        "text": "持有待售负债"
      },
      {
        "left": 883,
        "right": 937,
        "top": 284,
        "bottom": 318,
        "center_x": 910.0,
        "center_y": 301.0,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 1054,
        "bottom": 1087,
        "center_x": 193.0,
        "center_y": 1070.5,
        "text": "油气资产"
      },
      {
        "left": 856,
        "right": 883,
        "top": 318,
        "bottom": 351,
        "center_x": 869.5,
        "center_y": 334.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 852,
        "bottom": 886,
        "center_x": 399.5,
        "center_y": 869.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 185,
        "bottom": 217,
        "center_x": 1070.5,
        "center_y": 201.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 385,
        "bottom": 418,
        "center_x": 827.5,
        "center_y": 401.5,
        "text": "-40"
      },
      {
        "left": 937,
        "right": 999,
        "top": 250,
        "bottom": 284,
        "center_x": 968.0,
        "center_y": 267.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 718,
        "bottom": 752,
        "center_x": 542.5,
        "center_y": 735.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 919,
        "bottom": 952,
        "center_x": 299.5,
        "center_y": 935.5,
        "text": "21"
      },
      {
        "left": 614,
        "right": 799,
        "top": 586,
        "bottom": 618,
        "center_x": 706.5,
        "center_y": 602.0,
        "text": "一年内到期的非流动负债"
      },
      {
        "left": 883,
        "right": 937,
        "top": 318,
        "bottom": 351,
        "center_x": 910.0,
        "center_y": 334.5,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 1087,
        "bottom": 1120,
        "center_x": 193.0,
        "center_y": 1103.5,
        "text": "使用权资产"
      },
      {
        "left": 856,
        "right": 883,
        "top": 351,
        "bottom": 385,
        "center_x": 869.5,
        "center_y": 368.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 886,
        "bottom": 919,
        "center_x": 399.5,
        "center_y": 902.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 217,
        "bottom": 250,
        "center_x": 1070.5,
        "center_y": 233.5,
        "text": "24,900,000.00"
      },
      {
        "left": 799,
        "right": 856,
        "top": 418,
        "bottom": 452,
        "center_x": 827.5,
        "center_y": 435.0,
        "text": "41"
      },
      {
        "left": 937,
        "right": 999,
        "top": 284,
        "bottom": 318,
        "center_x": 968.0,
        "center_y": 301.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 752,
        "bottom": 786,
        "center_x": 542.5,
        "center_y": 769.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 952,
        "bottom": 986,
        "center_x": 299.5,
        "center_y": 969.0,
        "text": "22"
      },
      {
        "left": 614,
        "right": 799,
        "top": 618,
        "bottom": 652,
        "center_x": 706.5,
        "center_y": 635.0,
        "text": "其他流动负债"
      },
      {
        "left": 883,
        "right": 937,
        "top": 351,
        "bottom": 385,
        "center_x": 910.0,
        "center_y": 368.0,
        "text": "10,44"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1120,
        "bottom": 1153,
        "center_x": 193.0,
        "center_y": 1136.5,
        "text": "无形资产"
      },
      {
        "left": 856,
        "right": 883,
        "top": 385,
        "bottom": 418,
        "center_x": 869.5,
        "center_y": 401.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 919,
        "bottom": 952,
        "center_x": 399.5,
        "center_y": 935.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 250,
        "bottom": 284,
        "center_x": 1070.5,
        "center_y": 267.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 452,
        "bottom": 484,
        "center_x": 827.5,
        "center_y": 468.0,
        "text": "42"
      },
      {
        "left": 937,
        "right": 999,
        "top": 318,
        "bottom": 351,
        "center_x": 968.0,
        "center_y": 334.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 786,
        "bottom": 820,
        "center_x": 542.5,
        "center_y": 803.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 986,
        "bottom": 1020,
        "center_x": 299.5,
        "center_y": 1003.0,
        "text": "23"
      },
      {
        "left": 614,
        "right": 799,
        "top": 652,
        "bottom": 685,
        "center_x": 706.5,
        "center_y": 668.5,
        "text": "流动负债合计"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1153,
        "bottom": 1187,
        "center_x": 193.0,
        "center_y": 1170.0,
        "text": "开发支出"
      },
      {
        "left": 883,
        "right": 937,
        "top": 385,
        "bottom": 418,
        "center_x": 910.0,
        "center_y": 401.5,
        "text": "9,59"
      },
      {
        "left": 856,
        "right": 883,
        "top": 418,
        "bottom": 452,
        "center_x": 869.5,
        "center_y": 435.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 952,
        "bottom": 986,
        "center_x": 399.5,
        "center_y": 969.0,
        "text": "4,785,280.44"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 284,
        "bottom": 318,
        "center_x": 1070.5,
        "center_y": 301.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 484,
        "bottom": 518,
        "center_x": 827.5,
        "center_y": 501.0,
        "text": "43"
      },
      {
        "left": 937,
        "right": 999,
        "top": 351,
        "bottom": 385,
        "center_x": 968.0,
        "center_y": 368.0,
        "text": "4,413.76"
      },
      {
        "left": 471,
        "right": 614,
        "top": 820,
        "bottom": 852,
        "center_x": 542.5,
        "center_y": 836.0,
        "text": "1,000,000.00"
      },
      {
        "left": 271,
        "right": 328,
        "top": 1020,
        "bottom": 1054,
        "center_x": 299.5,
        "center_y": 1037.0,
        "text": "24"
      },
      {
        "left": 614,
        "right": 799,
        "top": 685,
        "bottom": 718,
        "center_x": 706.5,
        "center_y": 701.5,
        "text": "非流动负债："
      },
      {
        "left": 883,
        "right": 937,
        "top": 418,
        "bottom": 452,
        "center_x": 910.0,
        "center_y": 435.0,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 1187,
        "bottom": 1220,
        "center_x": 193.0,
        "center_y": 1203.5,
        "text": "商誉"
      },
      {
        "left": 856,
        "right": 883,
        "top": 452,
        "bottom": 484,
        "center_x": 869.5,
        "center_y": 468.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 986,
        "bottom": 1020,
        "center_x": 399.5,
        "center_y": 1003.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 318,
        "bottom": 351,
        "center_x": 1070.5,
        "center_y": 334.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 518,
        "bottom": 552,
        "center_x": 827.5,
        "center_y": 535.0,
        "text": "44"
      },
      {
        "left": 937,
        "right": 999,
        "top": 385,
        "bottom": 418,
        "center_x": 968.0,
        "center_y": 401.5,
        "text": "5,142.62"
      },
      {
        "left": 471,
        "right": 614,
        "top": 852,
        "bottom": 886,
        "center_x": 542.5,
        "center_y": 869.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1054,
        "bottom": 1087,
        "center_x": 299.5,
        "center_y": 1070.5,
        "text": "25"
      },
      {
        "left": 614,
        "right": 799,
        "top": 718,
        "bottom": 752,
        "center_x": 706.5,
        "center_y": 735.0,
        "text": "长期借款"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1220,
        "bottom": 1253,
        "center_x": 193.0,
        "center_y": 1236.5,
        "text": "长期待摊费用"
      },
      {
        "left": 883,
        "right": 937,
        "top": 452,
        "bottom": 484,
        "center_x": 910.0,
        "center_y": 468.0,
        "text": "1,15"
      },
      {
        "left": 856,
        "right": 883,
        "top": 484,
        "bottom": 518,
        "center_x": 869.5,
        "center_y": 501.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1020,
        "bottom": 1054,
        "center_x": 399.5,
        "center_y": 1037.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 351,
        "bottom": 385,
        "center_x": 1070.5,
        "center_y": 368.0,
        "text": "21,448,842.02"
      },
      {
        "left": 799,
        "right": 856,
        "top": 552,
        "bottom": 586,
        "center_x": 827.5,
        "center_y": 569.0,
        "text": "45"
      },
      {
        "left": 937,
        "right": 999,
        "top": 418,
        "bottom": 452,
        "center_x": 968.0,
        "center_y": 435.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 886,
        "bottom": 919,
        "center_x": 542.5,
        "center_y": 902.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1087,
        "bottom": 1120,
        "center_x": 299.5,
        "center_y": 1103.5,
        "text": "26"
      },
      {
        "left": 614,
        "right": 799,
        "top": 752,
        "bottom": 786,
        "center_x": 706.5,
        "center_y": 769.0,
        "text": "应付债券"
      },
      {
        "left": 883,
        "right": 937,
        "top": 484,
        "bottom": 518,
        "center_x": 910.0,
        "center_y": 501.0,
        "text": "72"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1253,
        "bottom": 1287,
        "center_x": 193.0,
        "center_y": 1270.0,
        "text": "递延所得税资产"
      },
      {
        "left": 856,
        "right": 883,
        "top": 518,
        "bottom": 552,
        "center_x": 869.5,
        "center_y": 535.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1054,
        "bottom": 1087,
        "center_x": 399.5,
        "center_y": 1070.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 385,
        "bottom": 418,
        "center_x": 1070.5,
        "center_y": 401.5,
        "text": "3,132,477.58"
      },
      {
        "left": 799,
        "right": 856,
        "top": 586,
        "bottom": 618,
        "center_x": 827.5,
        "center_y": 602.0,
        "text": "46"
      },
      {
        "left": 937,
        "right": 999,
        "top": 452,
        "bottom": 484,
        "center_x": 968.0,
        "center_y": 468.0,
        "text": "4,038.87"
      },
      {
        "left": 471,
        "right": 614,
        "top": 919,
        "bottom": 952,
        "center_x": 542.5,
        "center_y": 935.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1120,
        "bottom": 1153,
        "center_x": 299.5,
        "center_y": 1136.5,
        "text": "27"
      },
      {
        "left": 614,
        "right": 799,
        "top": 786,
        "bottom": 820,
        "center_x": 706.5,
        "center_y": 803.0,
        "text": "其中：优先股"
      },
      {
        "left": 883,
        "right": 937,
        "top": 518,
        "bottom": 552,
        "center_x": 910.0,
        "center_y": 535.0,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 1287,
        "bottom": 1320,
        "center_x": 193.0,
        "center_y": 1303.5,
        "text": "其他非流动资产"
      },
      {
        "left": 856,
        "right": 937,
        "top": 552,
        "bottom": 586,
        "center_x": 896.5,
        "center_y": 569.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1087,
        "bottom": 1120,
        "center_x": 399.5,
        "center_y": 1103.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 418,
        "bottom": 452,
        "center_x": 1070.5,
        "center_y": 435.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 618,
        "bottom": 652,
        "center_x": 827.5,
        "center_y": 635.0,
        "text": "47"
      },
      {
        "left": 937,
        "right": 999,
        "top": 484,
        "bottom": 518,
        "center_x": 968.0,
        "center_y": 501.0,
        "text": "5,382.80"
      },
      {
        "left": 471,
        "right": 614,
        "top": 952,
        "bottom": 986,
        "center_x": 542.5,
        "center_y": 969.0,
        "text": "9,482,561.29"
      },
      {
        "left": 271,
        "right": 328,
        "top": 1153,
        "bottom": 1187,
        "center_x": 299.5,
        "center_y": 1170.0,
        "text": "28"
      },
      {
        "left": 614,
        "right": 799,
        "top": 820,
        "bottom": 852,
        "center_x": 706.5,
        "center_y": 836.0,
        "text": "永续债"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1320,
        "bottom": 1354,
        "center_x": 193.0,
        "center_y": 1337.0,
        "text": "非流动资产合计"
      },
      {
        "left": 856,
        "right": 883,
        "top": 586,
        "bottom": 618,
        "center_x": 869.5,
        "center_y": 602.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1120,
        "bottom": 1153,
        "center_x": 399.5,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 452,
        "bottom": 484,
        "center_x": 1070.5,
        "center_y": 468.0,
        "text": "1,821,607.55"
      },
      {
        "left": 799,
        "right": 856,
        "top": 652,
        "bottom": 685,
        "center_x": 827.5,
        "center_y": 668.5,
        "text": "48"
      },
      {
        "left": 937,
        "right": 999,
        "top": 518,
        "bottom": 552,
        "center_x": 968.0,
        "center_y": 535.0,
        "text": "9,950.00"
      },
      {
        "left": 471,
        "right": 614,
        "top": 986,
        "bottom": 1020,
        "center_x": 542.5,
        "center_y": 1003.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1187,
        "bottom": 1220,
        "center_x": 299.5,
        "center_y": 1203.5,
        "text": "29"
      },
      {
        "left": 614,
        "right": 799,
        "top": 852,
        "bottom": 886,
        "center_x": 706.5,
        "center_y": 869.0,
        "text": "租赁负债"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1354,
        "bottom": 1387,
        "center_x": 193.0,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 586,
        "bottom": 618,
        "center_x": 910.0,
        "center_y": 602.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 618,
        "bottom": 652,
        "center_x": 869.5,
        "center_y": 635.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1153,
        "bottom": 1187,
        "center_x": 399.5,
        "center_y": 1170.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 484,
        "bottom": 518,
        "center_x": 1070.5,
        "center_y": 501.0,
        "text": "1,024,578.93"
      },
      {
        "left": 799,
        "right": 856,
        "top": 685,
        "bottom": 718,
        "center_x": 827.5,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 552,
        "bottom": 586,
        "center_x": 968.0,
        "center_y": 569.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1020,
        "bottom": 1054,
        "center_x": 542.5,
        "center_y": 1037.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1220,
        "bottom": 1253,
        "center_x": 299.5,
        "center_y": 1236.5,
        "text": "30"
      },
      {
        "left": 614,
        "right": 799,
        "top": 886,
        "bottom": 919,
        "center_x": 706.5,
        "center_y": 902.5,
        "text": "长期应付款"
      },
      {
        "left": 883,
        "right": 937,
        "top": 618,
        "bottom": 652,
        "center_x": 910.0,
        "center_y": 635.0,
        "text": "3"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1387,
        "bottom": 1419,
        "center_x": 193.0,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 652,
        "bottom": 685,
        "center_x": 869.5,
        "center_y": 668.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1187,
        "bottom": 1220,
        "center_x": 399.5,
        "center_y": 1203.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 518,
        "bottom": 552,
        "center_x": 1070.5,
        "center_y": 535.0,
        "text": "1,962,598.86"
      },
      {
        "left": 799,
        "right": 856,
        "top": 718,
        "bottom": 752,
        "center_x": 827.5,
        "center_y": 735.0,
        "text": "49"
      },
      {
        "left": 937,
        "right": 999,
        "top": 586,
        "bottom": 618,
        "center_x": 968.0,
        "center_y": 602.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1253,
        "bottom": 1287,
        "center_x": 299.5,
        "center_y": 1270.0,
        "text": "31"
      },
      {
        "left": 471,
        "right": 614,
        "top": 1054,
        "bottom": 1087,
        "center_x": 542.5,
        "center_y": 1070.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 919,
        "bottom": 952,
        "center_x": 706.5,
        "center_y": 935.5,
        "text": "预计负债"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1419,
        "bottom": 1452,
        "center_x": 193.0,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 652,
        "bottom": 685,
        "center_x": 910.0,
        "center_y": 668.5,
        "text": "46,86"
      },
      {
        "left": 856,
        "right": 883,
        "top": 685,
        "bottom": 718,
        "center_x": 869.5,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1220,
        "bottom": 1253,
        "center_x": 399.5,
        "center_y": 1236.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 552,
        "bottom": 586,
        "center_x": 1070.5,
        "center_y": 569.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 752,
        "bottom": 786,
        "center_x": 827.5,
        "center_y": 769.0,
        "text": "50"
      },
      {
        "left": 937,
        "right": 999,
        "top": 618,
        "bottom": 652,
        "center_x": 968.0,
        "center_y": 635.0,
        "text": "3,247.42"
      },
      {
        "left": 471,
        "right": 614,
        "top": 1087,
        "bottom": 1120,
        "center_x": 542.5,
        "center_y": 1103.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1287,
        "bottom": 1320,
        "center_x": 299.5,
        "center_y": 1303.5,
        "text": "32"
      },
      {
        "left": 614,
        "right": 799,
        "top": 952,
        "bottom": 986,
        "center_x": 706.5,
        "center_y": 969.0,
        "text": "递延收益"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1452,
        "bottom": 1485,
        "center_x": 193.0,
        "center_y": 1468.5,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 685,
        "bottom": 718,
        "center_x": 910.0,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 718,
        "bottom": 752,
        "center_x": 869.5,
        "center_y": 735.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1253,
        "bottom": 1287,
        "center_x": 399.5,
        "center_y": 1270.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 586,
        "bottom": 618,
        "center_x": 1070.5,
        "center_y": 602.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 786,
        "bottom": 820,
        "center_x": 827.5,
        "center_y": 803.0,
        "text": "51"
      },
      {
        "left": 937,
        "right": 999,
        "top": 652,
        "bottom": 685,
        "center_x": 968.0,
        "center_y": 668.5,
        "text": "2,175.47"
      },
      {
        "left": 471,
        "right": 614,
        "top": 1120,
        "bottom": 1153,
        "center_x": 542.5,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1320,
        "bottom": 1354,
        "center_x": 299.5,
        "center_y": 1337.0,
        "text": "33"
      },
      {
        "left": 115,
        "right": 271,
        "top": 1485,
        "bottom": 1518,
        "center_x": 193.0,
        "center_y": 1501.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 986,
        "bottom": 1020,
        "center_x": 706.5,
        "center_y": 1003.0,
        "text": "递延所得税负债"
      },
      {
        "left": 883,
        "right": 937,
        "top": 718,
        "bottom": 752,
        "center_x": 910.0,
        "center_y": 735.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 752,
        "bottom": 786,
        "center_x": 869.5,
        "center_y": 769.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1287,
        "bottom": 1320,
        "center_x": 399.5,
        "center_y": 1303.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 618,
        "bottom": 652,
        "center_x": 1070.5,
        "center_y": 635.0,
        "text": "39,627.22"
      },
      {
        "left": 799,
        "right": 856,
        "top": 820,
        "bottom": 852,
        "center_x": 827.5,
        "center_y": 836.0,
        "text": "52"
      },
      {
        "left": 937,
        "right": 999,
        "top": 685,
        "bottom": 718,
        "center_x": 968.0,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1153,
        "bottom": 1187,
        "center_x": 542.5,
        "center_y": 1170.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1354,
        "bottom": 1387,
        "center_x": 299.5,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 115,
        "right": 271,
        "top": 1518,
        "bottom": 1551,
        "center_x": 193.0,
        "center_y": 1534.5,
        "text": "资产总计"
      },
      {
        "left": 614,
        "right": 799,
        "top": 1020,
        "bottom": 1054,
        "center_x": 706.5,
        "center_y": 1037.0,
        "text": "其他非流动负债"
      },
      {
        "left": 883,
        "right": 937,
        "top": 752,
        "bottom": 786,
        "center_x": 910.0,
        "center_y": 769.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 786,
        "bottom": 820,
        "center_x": 869.5,
        "center_y": 803.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1320,
        "bottom": 1354,
        "center_x": 399.5,
        "center_y": 1337.0,
        "text": "7,267,612.85"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 652,
        "bottom": 685,
        "center_x": 1070.5,
        "center_y": 668.5,
        "text": "54,329,732.16"
      },
      {
        "left": 799,
        "right": 856,
        "top": 852,
        "bottom": 886,
        "center_x": 827.5,
        "center_y": 869.0,
        "text": "53"
      },
      {
        "left": 937,
        "right": 999,
        "top": 718,
        "bottom": 752,
        "center_x": 968.0,
        "center_y": 735.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1187,
        "bottom": 1220,
        "center_x": 542.5,
        "center_y": 1203.5,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1387,
        "bottom": 1419,
        "center_x": 299.5,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1054,
        "bottom": 1087,
        "center_x": 706.5,
        "center_y": 1070.5,
        "text": "非流动负债合计"
      },
      {
        "left": 883,
        "right": 937,
        "top": 786,
        "bottom": 820,
        "center_x": 910.0,
        "center_y": 803.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 820,
        "bottom": 852,
        "center_x": 869.5,
        "center_y": 836.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1354,
        "bottom": 1387,
        "center_x": 399.5,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 685,
        "bottom": 718,
        "center_x": 1070.5,
        "center_y": 701.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 886,
        "bottom": 919,
        "center_x": 827.5,
        "center_y": 902.5,
        "text": "54"
      },
      {
        "left": 937,
        "right": 999,
        "top": 752,
        "bottom": 786,
        "center_x": 968.0,
        "center_y": 769.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1419,
        "bottom": 1452,
        "center_x": 299.5,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1220,
        "bottom": 1253,
        "center_x": 542.5,
        "center_y": 1236.5,
        "text": "17,730,307.57"
      },
      {
        "left": 614,
        "right": 799,
        "top": 1087,
        "bottom": 1120,
        "center_x": 706.5,
        "center_y": 1103.5,
        "text": "负债合计"
      },
      {
        "left": 883,
        "right": 937,
        "top": 820,
        "bottom": 852,
        "center_x": 910.0,
        "center_y": 836.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 852,
        "bottom": 886,
        "center_x": 869.5,
        "center_y": 869.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1387,
        "bottom": 1419,
        "center_x": 399.5,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 718,
        "bottom": 752,
        "center_x": 1070.5,
        "center_y": 735.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 919,
        "bottom": 952,
        "center_x": 827.5,
        "center_y": 935.5,
        "text": "55"
      },
      {
        "left": 937,
        "right": 999,
        "top": 786,
        "bottom": 820,
        "center_x": 968.0,
        "center_y": 803.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1452,
        "bottom": 1485,
        "center_x": 299.5,
        "center_y": 1468.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1253,
        "bottom": 1287,
        "center_x": 542.5,
        "center_y": 1270.0,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1120,
        "bottom": 1153,
        "center_x": 706.5,
        "center_y": 1136.5,
        "text": "所有者权益（或股东权益）："
      },
      {
        "left": 883,
        "right": 937,
        "top": 852,
        "bottom": 886,
        "center_x": 910.0,
        "center_y": 869.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 886,
        "bottom": 919,
        "center_x": 869.5,
        "center_y": 902.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1419,
        "bottom": 1452,
        "center_x": 399.5,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 752,
        "bottom": 786,
        "center_x": 1070.5,
        "center_y": 769.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 952,
        "bottom": 986,
        "center_x": 827.5,
        "center_y": 969.0,
        "text": "56"
      },
      {
        "left": 271,
        "right": 328,
        "top": 1485,
        "bottom": 1518,
        "center_x": 299.5,
        "center_y": 1501.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 820,
        "bottom": 852,
        "center_x": 968.0,
        "center_y": 836.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1287,
        "bottom": 1320,
        "center_x": 542.5,
        "center_y": 1303.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1153,
        "bottom": 1187,
        "center_x": 706.5,
        "center_y": 1170.0,
        "text": "实收资本（或股本）"
      },
      {
        "left": 883,
        "right": 937,
        "top": 886,
        "bottom": 919,
        "center_x": 910.0,
        "center_y": 902.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 919,
        "bottom": 952,
        "center_x": 869.5,
        "center_y": 935.5,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1452,
        "bottom": 1485,
        "center_x": 399.5,
        "center_y": 1468.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 786,
        "bottom": 820,
        "center_x": 1070.5,
        "center_y": 803.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 986,
        "bottom": 1020,
        "center_x": 827.5,
        "center_y": 1003.0,
        "text": "57"
      },
      {
        "left": 937,
        "right": 999,
        "top": 852,
        "bottom": 886,
        "center_x": 968.0,
        "center_y": 869.0,
        "text": ""
      },
      {
        "left": 271,
        "right": 328,
        "top": 1518,
        "bottom": 1551,
        "center_x": 299.5,
        "center_y": 1534.5,
        "text": "34"
      },
      {
        "left": 471,
        "right": 614,
        "top": 1320,
        "bottom": 1354,
        "center_x": 542.5,
        "center_y": 1337.0,
        "text": "28,212,868.86"
      },
      {
        "left": 614,
        "right": 799,
        "top": 1187,
        "bottom": 1220,
        "center_x": 706.5,
        "center_y": 1203.5,
        "text": "其他权益工具"
      },
      {
        "left": 883,
        "right": 937,
        "top": 919,
        "bottom": 952,
        "center_x": 910.0,
        "center_y": 935.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 952,
        "bottom": 986,
        "center_x": 869.5,
        "center_y": 969.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1485,
        "bottom": 1518,
        "center_x": 399.5,
        "center_y": 1501.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 820,
        "bottom": 852,
        "center_x": 1070.5,
        "center_y": 836.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1020,
        "bottom": 1054,
        "center_x": 827.5,
        "center_y": 1037.0,
        "text": "58"
      },
      {
        "left": 937,
        "right": 999,
        "top": 886,
        "bottom": 919,
        "center_x": 968.0,
        "center_y": 902.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1354,
        "bottom": 1387,
        "center_x": 542.5,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1220,
        "bottom": 1253,
        "center_x": 706.5,
        "center_y": 1236.5,
        "text": "其中：优先股"
      },
      {
        "left": 883,
        "right": 937,
        "top": 952,
        "bottom": 986,
        "center_x": 910.0,
        "center_y": 969.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 986,
        "bottom": 1020,
        "center_x": 869.5,
        "center_y": 1003.0,
        "text": ""
      },
      {
        "left": 328,
        "right": 471,
        "top": 1518,
        "bottom": 1551,
        "center_x": 399.5,
        "center_y": 1534.5,
        "text": "84,167,782.95"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 852,
        "bottom": 886,
        "center_x": 1070.5,
        "center_y": 869.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1054,
        "bottom": 1087,
        "center_x": 827.5,
        "center_y": 1070.5,
        "text": "59"
      },
      {
        "left": 937,
        "right": 999,
        "top": 919,
        "bottom": 952,
        "center_x": 968.0,
        "center_y": 935.5,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1387,
        "bottom": 1419,
        "center_x": 542.5,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1253,
        "bottom": 1287,
        "center_x": 706.5,
        "center_y": 1270.0,
        "text": "永续债"
      },
      {
        "left": 883,
        "right": 937,
        "top": 986,
        "bottom": 1020,
        "center_x": 910.0,
        "center_y": 1003.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1020,
        "bottom": 1054,
        "center_x": 869.5,
        "center_y": 1037.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 886,
        "bottom": 919,
        "center_x": 1070.5,
        "center_y": 902.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1087,
        "bottom": 1120,
        "center_x": 827.5,
        "center_y": 1103.5,
        "text": "60"
      },
      {
        "left": 937,
        "right": 999,
        "top": 952,
        "bottom": 986,
        "center_x": 968.0,
        "center_y": 969.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1419,
        "bottom": 1452,
        "center_x": 542.5,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1287,
        "bottom": 1320,
        "center_x": 706.5,
        "center_y": 1303.5,
        "text": "资本公积"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1020,
        "bottom": 1054,
        "center_x": 910.0,
        "center_y": 1037.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1054,
        "bottom": 1087,
        "center_x": 869.5,
        "center_y": 1070.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 919,
        "bottom": 952,
        "center_x": 1070.5,
        "center_y": 935.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1120,
        "bottom": 1153,
        "center_x": 827.5,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 986,
        "bottom": 1020,
        "center_x": 968.0,
        "center_y": 1003.0,
        "text": ""
      },
      {
        "left": 471,
        "right": 614,
        "top": 1452,
        "bottom": 1485,
        "center_x": 542.5,
        "center_y": 1468.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1320,
        "bottom": 1354,
        "center_x": 706.5,
        "center_y": 1337.0,
        "text": "减：库存股"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1054,
        "bottom": 1087,
        "center_x": 910.0,
        "center_y": 1070.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1087,
        "bottom": 1120,
        "center_x": 869.5,
        "center_y": 1103.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 952,
        "bottom": 986,
        "center_x": 1070.5,
        "center_y": 969.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1153,
        "bottom": 1187,
        "center_x": 827.5,
        "center_y": 1170.0,
        "text": "61"
      },
      {
        "left": 471,
        "right": 614,
        "top": 1485,
        "bottom": 1518,
        "center_x": 542.5,
        "center_y": 1501.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1020,
        "bottom": 1054,
        "center_x": 968.0,
        "center_y": 1037.0,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1354,
        "bottom": 1387,
        "center_x": 706.5,
        "center_y": 1370.5,
        "text": "其他综合收益"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1087,
        "bottom": 1120,
        "center_x": 910.0,
        "center_y": 1103.5,
        "text": "46,86"
      },
      {
        "left": 856,
        "right": 883,
        "top": 1120,
        "bottom": 1153,
        "center_x": 869.5,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 986,
        "bottom": 1020,
        "center_x": 1070.5,
        "center_y": 1003.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1187,
        "bottom": 1220,
        "center_x": 827.5,
        "center_y": 1203.5,
        "text": "62"
      },
      {
        "left": 471,
        "right": 614,
        "top": 1518,
        "bottom": 1551,
        "center_x": 542.5,
        "center_y": 1534.5,
        "text": "87,249,229.63"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1054,
        "bottom": 1087,
        "center_x": 968.0,
        "center_y": 1070.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1387,
        "bottom": 1419,
        "center_x": 706.5,
        "center_y": 1403.0,
        "text": "专项储备"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1120,
        "bottom": 1153,
        "center_x": 910.0,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1153,
        "bottom": 1187,
        "center_x": 869.5,
        "center_y": 1170.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1020,
        "bottom": 1054,
        "center_x": 1070.5,
        "center_y": 1037.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1220,
        "bottom": 1253,
        "center_x": 827.5,
        "center_y": 1236.5,
        "text": "63"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1087,
        "bottom": 1120,
        "center_x": 968.0,
        "center_y": 1103.5,
        "text": "2,175.47"
      },
      {
        "left": 614,
        "right": 799,
        "top": 1419,
        "bottom": 1452,
        "center_x": 706.5,
        "center_y": 1435.5,
        "text": "盈余公积"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1153,
        "bottom": 1187,
        "center_x": 910.0,
        "center_y": 1170.0,
        "text": "20,00"
      },
      {
        "left": 856,
        "right": 883,
        "top": 1187,
        "bottom": 1220,
        "center_x": 869.5,
        "center_y": 1203.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1253,
        "bottom": 1287,
        "center_x": 827.5,
        "center_y": 1270.0,
        "text": "64"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1054,
        "bottom": 1087,
        "center_x": 1070.5,
        "center_y": 1070.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1120,
        "bottom": 1153,
        "center_x": 968.0,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1452,
        "bottom": 1485,
        "center_x": 706.5,
        "center_y": 1468.5,
        "text": "未分配利润"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1187,
        "bottom": 1220,
        "center_x": 910.0,
        "center_y": 1203.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1220,
        "bottom": 1253,
        "center_x": 869.5,
        "center_y": 1236.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1087,
        "bottom": 1120,
        "center_x": 1070.5,
        "center_y": 1103.5,
        "text": "54,329,732.16"
      },
      {
        "left": 799,
        "right": 856,
        "top": 1287,
        "bottom": 1320,
        "center_x": 827.5,
        "center_y": 1303.5,
        "text": "65"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1153,
        "bottom": 1187,
        "center_x": 968.0,
        "center_y": 1170.0,
        "text": "0,000.00"
      },
      {
        "left": 614,
        "right": 799,
        "top": 1485,
        "bottom": 1518,
        "center_x": 706.5,
        "center_y": 1501.5,
        "text": "所有者权益（或股东权益）合计"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1220,
        "bottom": 1253,
        "center_x": 910.0,
        "center_y": 1236.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1253,
        "bottom": 1287,
        "center_x": 869.5,
        "center_y": 1270.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1120,
        "bottom": 1153,
        "center_x": 1070.5,
        "center_y": 1136.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1320,
        "bottom": 1354,
        "center_x": 827.5,
        "center_y": 1337.0,
        "text": "66"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1187,
        "bottom": 1220,
        "center_x": 968.0,
        "center_y": 1203.5,
        "text": ""
      },
      {
        "left": 614,
        "right": 799,
        "top": 1518,
        "bottom": 1551,
        "center_x": 706.5,
        "center_y": 1534.5,
        "text": "负债和所有者权益（或股东权益 ）总计"
      },
      {
        "left": 883,
        "right": 937,
        "top": 1253,
        "bottom": 1287,
        "center_x": 910.0,
        "center_y": 1270.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1287,
        "bottom": 1320,
        "center_x": 869.5,
        "center_y": 1303.5,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1153,
        "bottom": 1187,
        "center_x": 1070.5,
        "center_y": 1170.0,
        "text": "20,000,000.00"
      },
      {
        "left": 799,
        "right": 856,
        "top": 1354,
        "bottom": 1387,
        "center_x": 827.5,
        "center_y": 1370.5,
        "text": "67"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1220,
        "bottom": 1253,
        "center_x": 968.0,
        "center_y": 1236.5,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 1287,
        "bottom": 1320,
        "center_x": 910.0,
        "center_y": 1303.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1320,
        "bottom": 1354,
        "center_x": 869.5,
        "center_y": 1337.0,
        "text": ""
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1187,
        "bottom": 1220,
        "center_x": 1070.5,
        "center_y": 1203.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1387,
        "bottom": 1419,
        "center_x": 827.5,
        "center_y": 1403.0,
        "text": "68"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1253,
        "bottom": 1287,
        "center_x": 968.0,
        "center_y": 1270.0,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 1320,
        "bottom": 1354,
        "center_x": 910.0,
        "center_y": 1337.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1354,
        "bottom": 1387,
        "center_x": 869.5,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1419,
        "bottom": 1452,
        "center_x": 827.5,
        "center_y": 1435.5,
        "text": "69"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1220,
        "bottom": 1253,
        "center_x": 1070.5,
        "center_y": 1236.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1287,
        "bottom": 1320,
        "center_x": 968.0,
        "center_y": 1303.5,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 1354,
        "bottom": 1387,
        "center_x": 910.0,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 883,
        "top": 1387,
        "bottom": 1419,
        "center_x": 869.5,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1452,
        "bottom": 1485,
        "center_x": 827.5,
        "center_y": 1468.5,
        "text": "70"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1253,
        "bottom": 1287,
        "center_x": 1070.5,
        "center_y": 1270.0,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1320,
        "bottom": 1354,
        "center_x": 968.0,
        "center_y": 1337.0,
        "text": ""
      },
      {
        "left": 883,
        "right": 937,
        "top": 1387,
        "bottom": 1419,
        "center_x": 910.0,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 937,
        "top": 1419,
        "bottom": 1452,
        "center_x": 896.5,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 799,
        "right": 856,
        "top": 1485,
        "bottom": 1518,
        "center_x": 827.5,
        "center_y": 1501.5,
        "text": "71"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1287,
        "bottom": 1320,
        "center_x": 1070.5,
        "center_y": 1303.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1354,
        "bottom": 1387,
        "center_x": 968.0,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 937,
        "top": 1452,
        "bottom": 1485,
        "center_x": 896.5,
        "center_y": 1468.5,
        "text": "17,30"
      },
      {
        "left": 799,
        "right": 856,
        "top": 1518,
        "bottom": 1551,
        "center_x": 827.5,
        "center_y": 1534.5,
        "text": "72"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1320,
        "bottom": 1354,
        "center_x": 1070.5,
        "center_y": 1337.0,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1387,
        "bottom": 1419,
        "center_x": 968.0,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 856,
        "right": 937,
        "top": 1485,
        "bottom": 1518,
        "center_x": 896.5,
        "center_y": 1501.5,
        "text": "31,39"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1354,
        "bottom": 1387,
        "center_x": 1070.5,
        "center_y": 1370.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1419,
        "bottom": 1452,
        "center_x": 968.0,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 856,
        "right": 937,
        "top": 1518,
        "bottom": 1551,
        "center_x": 896.5,
        "center_y": 1534.5,
        "text": "P（84,16"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1387,
        "bottom": 1419,
        "center_x": 1070.5,
        "center_y": 1403.0,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1452,
        "bottom": 1485,
        "center_x": 968.0,
        "center_y": 1468.5,
        "text": "5,607.48"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1419,
        "bottom": 1452,
        "center_x": 1070.5,
        "center_y": 1435.5,
        "text": ""
      },
      {
        "left": 937,
        "right": 999,
        "top": 1485,
        "bottom": 1518,
        "center_x": 968.0,
        "center_y": 1501.5,
        "text": "5,607.48"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1452,
        "bottom": 1485,
        "center_x": 1070.5,
        "center_y": 1468.5,
        "text": "12,919,497.47"
      },
      {
        "left": 937,
        "right": 999,
        "top": 1518,
        "bottom": 1551,
        "center_x": 968.0,
        "center_y": 1534.5,
        "text": "7,782.95"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1485,
        "bottom": 1518,
        "center_x": 1070.5,
        "center_y": 1501.5,
        "text": "32,919,497.47"
      },
      {
        "left": 999,
        "right": 1142,
        "top": 1518,
        "bottom": 1551,
        "center_x": 1070.5,
        "center_y": 1534.5,
        "text": "87,249,229.63"
      }
    ],
    "range": {
      "left": 115,
      "right": 1142,
      "top": 126,
      "bottom": 1551,
      "center_x": 628.5,
      "center_y": 838.5
    },
    "text": "编制单位：苏州梅克兰循环科技有限公司 2022-12-31 资产 流动资产： 货币资金 交易性金融资产 衍生金融资产 行次 应收票据  应收账款 年初余额 1 应收款项融资  2 预付款项 21,627,911.73 3 其他应收款  4 存货  5 期末余额 合同资产   6 持有待售资产 26,330,584.17 15,709,953.27 7 一年内到期的非流动资产   8 其他流动资产 21,812,565.11  9 负债和所有者权益 流动资产合计 1,127,499.00  10 流动负债： 非流动资产： 5,377,878.14 33,701,842.62 11 短期借款 债权投资   12 交易性金融负债7 其他债权投资  2,038,269.74 13 衍生金融负债 长期应收款  1,036,020.00 14 应付票据 长期股权投资 623,731.95 行次 6,802,676.05  应付账款 其他权益工具投资 76,900,170.10   15 预收款项 其他非流动金融资产    35  16 合同负债 投资性房地产 年初   36  17 单位：元 应付职工薪酬 固定资产    37 余额 -252,400.91 18 应交税费 24,90 在建工程   38  59,036,360.77 19 其他应付款  生产性生物资产  2,482,332.41 39 期末余额 0,000.00  20 持有待售负债  油气资产    -40   21 一年内到期的非流动负债  使用权资产   24,900,000.00 41   22 其他流动负债 10,44 无形资产    42   23 流动负债合计 开发支出 9,59  4,785,280.44  43 4,413.76 1,000,000.00 24 非流动负债：  商誉    44 5,142.62  25 长期借款 长期待摊费用 1,15   21,448,842.02 45   26 应付债券 72 递延所得税资产   3,132,477.58 46 4,038.87  27 其中：优先股  其他非流动资产    47 5,382.80 9,482,561.29 28 永续债 非流动资产合计   1,821,607.55 48 9,950.00  29 租赁负债     1,024,578.93    30 长期应付款 3    1,962,598.86 49  31  预计负债  46,86    50 3,247.42  32 递延收益      51 2,175.47  33  递延所得税负债    39,627.22 52    资产总计 其他非流动负债   7,267,612.85 54,329,732.16 53    非流动负债合计     54   17,730,307.57 负债合计     55    所有者权益（或股东权益）：     56    实收资本（或股本）     57  34 28,212,868.86 其他权益工具     58   其中：优先股   84,167,782.95  59   永续债    60   资本公积       减：库存股    61   其他综合收益 46,86   62 87,249,229.63  专项储备    63 2,175.47 盈余公积 20,00  64   未分配利润   54,329,732.16 65 0,000.00 所有者权益（或股东权益）合计    66  负债和所有者权益（或股东权益 ）总计   20,000,000.00 67     68    69     70     71   17,30 72   31,39   P（84,16  5,607.48  5,607.48 12,919,497.47 7,782.95 32,919,497.47 87,249,229.63"
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 571.9417205763001,
      "right": 665.2823971429559,
      "top": 110.65808983741339,
      "bottom": 142.97976497516981,
      "center_x": 618.612058859628,
      "center_y": 126.8189274062916
    },
    "text": "利润表"
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 117.33920001983643,
      "right": 466.3037414550781,
      "top": 158.75587030102452,
      "bottom": 178.42468167484947,
      "center_x": 291.8214707374573,
      "center_y": 168.590275987937
    },
    "text": "编制单位：苏州梅克兰循环科技有限公司"
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 573.2477763727436,
      "right": 673.7289781570435,
      "top": 157.80620138175112,
      "bottom": 179.24869989914095,
      "center_x": 623.4883772648935,
      "center_y": 168.52745064044603
    },
    "text": "2022年12期"
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 1040.629473218235,
      "right": 1118.1556196212769,
      "top": 159.22239151297265,
      "bottom": 178.96177563649064,
      "center_x": 1079.392546419756,
      "center_y": 169.09208357473165
    },
    "text": "单位：元"
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 116.98841857910156,
      "right": 224.714363448189,
      "top": 1558.098368501196,
      "bottom": 1578.3027079194321,
      "center_x": 170.8513910136453,
      "center_y": 1568.200538210314
    },
    "text": "单位负责人："
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 453.0170841217041,
      "right": 560.9230412314339,
      "top": 1559.1202631624587,
      "bottom": 1579.0422202830414,
      "center_x": 506.970062676569,
      "center_y": 1569.08124172275
    },
    "text": "会计负责人："
  },
  {
    "page_id": 3,
    "type": "text",
    "range": {
      "left": 788.9353675842285,
      "right": 858.7206964492798,
      "top": 1560.150371855936,
      "bottom": 1579.8911251038369,
      "center_x": 823.8280320167542,
      "center_y": 1570.0207484798866
    },
    "text": "制表人：："
  },
  {
    "page_id": 3,
    "type": "table",
    "cells": [
      {
        "left": 115,
        "right": 517,
        "top": 190,
        "bottom": 218,
        "center_x": 316.0,
        "center_y": 204.0,
        "text": "项目"
      },
      {
        "left": 115,
        "right": 517,
        "top": 218,
        "bottom": 249,
        "center_x": 316.0,
        "center_y": 233.5,
        "text": "一、营业收入"
      },
      {
        "left": 115,
        "right": 517,
        "top": 249,
        "bottom": 278,
        "center_x": 316.0,
        "center_y": 263.5,
        "text": "减：营业成本"
      },
      {
        "left": 115,
        "right": 517,
        "top": 278,
        "bottom": 307,
        "center_x": 316.0,
        "center_y": 292.5,
        "text": "税金及附加"
      },
      {
        "left": 115,
        "right": 517,
        "top": 307,
        "bottom": 337,
        "center_x": 316.0,
        "center_y": 322.0,
        "text": "销售费用"
      },
      {
        "left": 115,
        "right": 517,
        "top": 337,
        "bottom": 366,
        "center_x": 316.0,
        "center_y": 351.5,
        "text": "管理费用"
      },
      {
        "left": 115,
        "right": 517,
        "top": 366,
        "bottom": 396,
        "center_x": 316.0,
        "center_y": 381.0,
        "text": "研发费用"
      },
      {
        "left": 115,
        "right": 517,
        "top": 396,
        "bottom": 425,
        "center_x": 316.0,
        "center_y": 410.5,
        "text": "财务费用"
      },
      {
        "left": 115,
        "right": 517,
        "top": 425,
        "bottom": 455,
        "center_x": 316.0,
        "center_y": 440.0,
        "text": "其中：利息费用"
      },
      {
        "left": 115,
        "right": 517,
        "top": 455,
        "bottom": 485,
        "center_x": 316.0,
        "center_y": 470.0,
        "text": "利息收入"
      },
      {
        "left": 115,
        "right": 517,
        "top": 485,
        "bottom": 514,
        "center_x": 316.0,
        "center_y": 499.5,
        "text": "加：其他收益"
      },
      {
        "left": 115,
        "right": 517,
        "top": 514,
        "bottom": 544,
        "center_x": 316.0,
        "center_y": 529.0,
        "text": "投资收益（损失以“-”号填列)"
      },
      {
        "left": 115,
        "right": 517,
        "top": 544,
        "bottom": 573,
        "center_x": 316.0,
        "center_y": 558.5,
        "text": "其中：对联营企业和合营企业的投资收益"
      },
      {
        "left": 115,
        "right": 517,
        "top": 573,
        "bottom": 602,
        "center_x": 316.0,
        "center_y": 587.5,
        "text": "以摊余成本计量的金融资产终止确认收益"
      },
      {
        "left": 517,
        "right": 567,
        "top": 190,
        "bottom": 218,
        "center_x": 542.0,
        "center_y": 204.0,
        "text": "行次"
      },
      {
        "left": 115,
        "right": 517,
        "top": 602,
        "bottom": 632,
        "center_x": 316.0,
        "center_y": 617.0,
        "text": "净敞口套期收益（损失以“-”号填列）"
      },
      {
        "left": 517,
        "right": 567,
        "top": 218,
        "bottom": 249,
        "center_x": 542.0,
        "center_y": 233.5,
        "text": "1"
      },
      {
        "left": 115,
        "right": 517,
        "top": 632,
        "bottom": 662,
        "center_x": 316.0,
        "center_y": 647.0,
        "text": "公允价值变动收益（损失以“-”号填列）"
      },
      {
        "left": 567,
        "right": 870,
        "top": 190,
        "bottom": 218,
        "center_x": 718.5,
        "center_y": 204.0,
        "text": "本期数"
      },
      {
        "left": 517,
        "right": 567,
        "top": 249,
        "bottom": 278,
        "center_x": 542.0,
        "center_y": 263.5,
        "text": "2"
      },
      {
        "left": 115,
        "right": 517,
        "top": 662,
        "bottom": 691,
        "center_x": 316.0,
        "center_y": 676.5,
        "text": "信用减值损失（损失以“-”号填列)"
      },
      {
        "left": 567,
        "right": 870,
        "top": 218,
        "bottom": 249,
        "center_x": 718.5,
        "center_y": 233.5,
        "text": "12,300,846.24"
      },
      {
        "left": 517,
        "right": 567,
        "top": 278,
        "bottom": 307,
        "center_x": 542.0,
        "center_y": 292.5,
        "text": "3"
      },
      {
        "left": 115,
        "right": 517,
        "top": 691,
        "bottom": 721,
        "center_x": 316.0,
        "center_y": 706.0,
        "text": "资产减值损失（损失以“-”号填列)"
      },
      {
        "left": 567,
        "right": 685,
        "top": 249,
        "bottom": 278,
        "center_x": 626.0,
        "center_y": 263.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 307,
        "bottom": 337,
        "center_x": 542.0,
        "center_y": 322.0,
        "text": "4"
      },
      {
        "left": 115,
        "right": 517,
        "top": 721,
        "bottom": 751,
        "center_x": 316.0,
        "center_y": 736.0,
        "text": "资产处置收益（损失以“-”号填列）"
      },
      {
        "left": 567,
        "right": 685,
        "top": 278,
        "bottom": 307,
        "center_x": 626.0,
        "center_y": 292.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 337,
        "bottom": 366,
        "center_x": 542.0,
        "center_y": 351.5,
        "text": "5"
      },
      {
        "left": 115,
        "right": 517,
        "top": 751,
        "bottom": 780,
        "center_x": 316.0,
        "center_y": 765.5,
        "text": "二、营业利润（亏损以“-”号填列）"
      },
      {
        "left": 567,
        "right": 685,
        "top": 307,
        "bottom": 337,
        "center_x": 626.0,
        "center_y": 322.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 366,
        "bottom": 396,
        "center_x": 542.0,
        "center_y": 381.0,
        "text": "6"
      },
      {
        "left": 115,
        "right": 517,
        "top": 780,
        "bottom": 809,
        "center_x": 316.0,
        "center_y": 794.5,
        "text": "加：营业外收入"
      },
      {
        "left": 567,
        "right": 870,
        "top": 337,
        "bottom": 366,
        "center_x": 718.5,
        "center_y": 351.5,
        "text": "2,606,207.88"
      },
      {
        "left": 517,
        "right": 567,
        "top": 396,
        "bottom": 425,
        "center_x": 542.0,
        "center_y": 410.5,
        "text": "7"
      },
      {
        "left": 115,
        "right": 517,
        "top": 809,
        "bottom": 839,
        "center_x": 316.0,
        "center_y": 824.0,
        "text": "减：营业外支出"
      },
      {
        "left": 567,
        "right": 870,
        "top": 366,
        "bottom": 396,
        "center_x": 718.5,
        "center_y": 381.0,
        "text": ""
      },
      {
        "left": 685,
        "right": 870,
        "top": 249,
        "bottom": 278,
        "center_x": 777.5,
        "center_y": 263.5,
        "text": ".11,359,680.41"
      },
      {
        "left": 517,
        "right": 567,
        "top": 425,
        "bottom": 455,
        "center_x": 542.0,
        "center_y": 440.0,
        "text": "8"
      },
      {
        "left": 115,
        "right": 517,
        "top": 839,
        "bottom": 868,
        "center_x": 316.0,
        "center_y": 853.5,
        "text": "三、利润总额（亏损总额以“-”号填列）"
      },
      {
        "left": 685,
        "right": 870,
        "top": 278,
        "bottom": 307,
        "center_x": 777.5,
        "center_y": 292.5,
        "text": "128,163.30"
      },
      {
        "left": 567,
        "right": 870,
        "top": 396,
        "bottom": 425,
        "center_x": 718.5,
        "center_y": 410.5,
        "text": "404,741.70"
      },
      {
        "left": 517,
        "right": 567,
        "top": 455,
        "bottom": 485,
        "center_x": 542.0,
        "center_y": 470.0,
        "text": "9"
      },
      {
        "left": 115,
        "right": 517,
        "top": 868,
        "bottom": 898,
        "center_x": 316.0,
        "center_y": 883.0,
        "text": "减：所得税费用"
      },
      {
        "left": 685,
        "right": 870,
        "top": 307,
        "bottom": 337,
        "center_x": 777.5,
        "center_y": 322.0,
        "text": "1,848,347.51"
      },
      {
        "left": 567,
        "right": 870,
        "top": 425,
        "bottom": 455,
        "center_x": 718.5,
        "center_y": 440.0,
        "text": "-10,775.80"
      },
      {
        "left": 517,
        "right": 567,
        "top": 485,
        "bottom": 514,
        "center_x": 542.0,
        "center_y": 499.5,
        "text": "10"
      },
      {
        "left": 115,
        "right": 517,
        "top": 898,
        "bottom": 928,
        "center_x": 316.0,
        "center_y": 913.0,
        "text": "四、净利润（净亏损以“-”号填列）"
      },
      {
        "left": 567,
        "right": 870,
        "top": 455,
        "bottom": 485,
        "center_x": 718.5,
        "center_y": 470.0,
        "text": "33,490.23"
      },
      {
        "left": 517,
        "right": 567,
        "top": 514,
        "bottom": 544,
        "center_x": 542.0,
        "center_y": 529.0,
        "text": "11"
      },
      {
        "left": 115,
        "right": 517,
        "top": 928,
        "bottom": 958,
        "center_x": 316.0,
        "center_y": 943.0,
        "text": "（一）持续经营净利润（净亏损以“-”号填列）"
      },
      {
        "left": 567,
        "right": 870,
        "top": 485,
        "bottom": 514,
        "center_x": 718.5,
        "center_y": 499.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 190,
        "bottom": 218,
        "center_x": 996.0,
        "center_y": 204.0,
        "text": "本年累计数"
      },
      {
        "left": 517,
        "right": 567,
        "top": 544,
        "bottom": 573,
        "center_x": 542.0,
        "center_y": 558.5,
        "text": "12"
      },
      {
        "left": 115,
        "right": 517,
        "top": 958,
        "bottom": 987,
        "center_x": 316.0,
        "center_y": 972.5,
        "text": "（二）终止经营净利润（净亏损以“-”号填列）"
      },
      {
        "left": 567,
        "right": 870,
        "top": 514,
        "bottom": 544,
        "center_x": 718.5,
        "center_y": 529.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 218,
        "bottom": 249,
        "center_x": 996.0,
        "center_y": 233.5,
        "text": "115,273,945.12"
      },
      {
        "left": 517,
        "right": 567,
        "top": 573,
        "bottom": 602,
        "center_x": 542.0,
        "center_y": 587.5,
        "text": "13"
      },
      {
        "left": 115,
        "right": 517,
        "top": 987,
        "bottom": 1016,
        "center_x": 316.0,
        "center_y": 1001.5,
        "text": "五、其他综合收益的税后净额"
      },
      {
        "left": 567,
        "right": 870,
        "top": 544,
        "bottom": 573,
        "center_x": 718.5,
        "center_y": 558.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 987,
        "top": 249,
        "bottom": 278,
        "center_x": 928.5,
        "center_y": 263.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 602,
        "bottom": 632,
        "center_x": 542.0,
        "center_y": 617.0,
        "text": "14"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1016,
        "bottom": 1046,
        "center_x": 316.0,
        "center_y": 1031.0,
        "text": "（一）不能重分类进损益的其他综合收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 573,
        "bottom": 602,
        "center_x": 718.5,
        "center_y": 587.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 904,
        "top": 278,
        "bottom": 307,
        "center_x": 887.0,
        "center_y": 292.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 632,
        "bottom": 662,
        "center_x": 542.0,
        "center_y": 647.0,
        "text": "15"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1046,
        "bottom": 1075,
        "center_x": 316.0,
        "center_y": 1060.5,
        "text": "1. 重新计量设定受益计划变动额"
      },
      {
        "left": 567,
        "right": 870,
        "top": 602,
        "bottom": 632,
        "center_x": 718.5,
        "center_y": 617.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 904,
        "top": 307,
        "bottom": 337,
        "center_x": 887.0,
        "center_y": 322.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 662,
        "bottom": 691,
        "center_x": 542.0,
        "center_y": 676.5,
        "text": "16"
      },
      {
        "left": 904,
        "right": 1122,
        "top": 278,
        "bottom": 307,
        "center_x": 1013.0,
        "center_y": 292.5,
        "text": "734,837.88"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1075,
        "bottom": 1105,
        "center_x": 316.0,
        "center_y": 1090.0,
        "text": "2.权益法下不能转损益的其他综合收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 632,
        "bottom": 662,
        "center_x": 718.5,
        "center_y": 647.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 337,
        "bottom": 366,
        "center_x": 996.0,
        "center_y": 351.5,
        "text": "19,807,751.68"
      },
      {
        "left": 517,
        "right": 567,
        "top": 691,
        "bottom": 721,
        "center_x": 542.0,
        "center_y": 706.0,
        "text": "17"
      },
      {
        "left": 904,
        "right": 1122,
        "top": 307,
        "bottom": 337,
        "center_x": 1013.0,
        "center_y": 322.0,
        "text": "20,007,546.08"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1105,
        "bottom": 1134,
        "center_x": 316.0,
        "center_y": 1119.5,
        "text": "3. 其他权益工具投资公允价值变动"
      },
      {
        "left": 567,
        "right": 870,
        "top": 662,
        "bottom": 691,
        "center_x": 718.5,
        "center_y": 676.5,
        "text": ""
      },
      {
        "left": 987,
        "right": 1122,
        "top": 249,
        "bottom": 278,
        "center_x": 1054.5,
        "center_y": 263.5,
        "text": "77,546,764.72"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 366,
        "bottom": 396,
        "center_x": 996.0,
        "center_y": 381.0,
        "text": "95,948.24"
      },
      {
        "left": 517,
        "right": 567,
        "top": 721,
        "bottom": 751,
        "center_x": 542.0,
        "center_y": 736.0,
        "text": "18"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1134,
        "bottom": 1164,
        "center_x": 316.0,
        "center_y": 1149.0,
        "text": "4. 企业自身信用风险公允价值变动"
      },
      {
        "left": 567,
        "right": 870,
        "top": 691,
        "bottom": 721,
        "center_x": 718.5,
        "center_y": 706.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 396,
        "bottom": 425,
        "center_x": 996.0,
        "center_y": 410.5,
        "text": "1,652,097.24"
      },
      {
        "left": 517,
        "right": 567,
        "top": 751,
        "bottom": 780,
        "center_x": 542.0,
        "center_y": 765.5,
        "text": "19"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1164,
        "bottom": 1194,
        "center_x": 316.0,
        "center_y": 1179.0,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 721,
        "bottom": 751,
        "center_x": 718.5,
        "center_y": 736.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 425,
        "bottom": 455,
        "center_x": 996.0,
        "center_y": 440.0,
        "text": "-49,105.24"
      },
      {
        "left": 517,
        "right": 567,
        "top": 780,
        "bottom": 809,
        "center_x": 542.0,
        "center_y": 794.5,
        "text": "20"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1194,
        "bottom": 1223,
        "center_x": 316.0,
        "center_y": 1208.5,
        "text": "（二）将重分类进损益的其他综合收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 751,
        "bottom": 780,
        "center_x": 718.5,
        "center_y": 765.5,
        "text": "-4,046,294.56"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 455,
        "bottom": 485,
        "center_x": 996.0,
        "center_y": 470.0,
        "text": "52,829.65"
      },
      {
        "left": 517,
        "right": 567,
        "top": 809,
        "bottom": 839,
        "center_x": 542.0,
        "center_y": 824.0,
        "text": "21"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1223,
        "bottom": 1253,
        "center_x": 316.0,
        "center_y": 1238.0,
        "text": "1. 权益法下可转损益的其他综合收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 780,
        "bottom": 809,
        "center_x": 718.5,
        "center_y": 794.5,
        "text": "-146,250.47"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 485,
        "bottom": 514,
        "center_x": 996.0,
        "center_y": 499.5,
        "text": "218,203.71"
      },
      {
        "left": 517,
        "right": 567,
        "top": 839,
        "bottom": 868,
        "center_x": 542.0,
        "center_y": 853.5,
        "text": "22"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1253,
        "bottom": 1281,
        "center_x": 316.0,
        "center_y": 1267.0,
        "text": "2.其他债权投资公允价值变动"
      },
      {
        "left": 567,
        "right": 870,
        "top": 809,
        "bottom": 839,
        "center_x": 718.5,
        "center_y": 824.0,
        "text": "76,249.04"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 514,
        "bottom": 544,
        "center_x": 996.0,
        "center_y": 529.0,
        "text": "221,633.41"
      },
      {
        "left": 517,
        "right": 567,
        "top": 868,
        "bottom": 898,
        "center_x": 542.0,
        "center_y": 883.0,
        "text": "23"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1281,
        "bottom": 1311,
        "center_x": 316.0,
        "center_y": 1296.0,
        "text": "3. 金融资产重分类计入其他综合收益的金额"
      },
      {
        "left": 567,
        "right": 870,
        "top": 839,
        "bottom": 868,
        "center_x": 718.5,
        "center_y": 853.5,
        "text": "-4,268,794.07"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 544,
        "bottom": 573,
        "center_x": 996.0,
        "center_y": 558.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 898,
        "bottom": 928,
        "center_x": 542.0,
        "center_y": 913.0,
        "text": "24"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1311,
        "bottom": 1341,
        "center_x": 316.0,
        "center_y": 1326.0,
        "text": "4. 其他债权投资信用减值准备"
      },
      {
        "left": 567,
        "right": 870,
        "top": 868,
        "bottom": 898,
        "center_x": 718.5,
        "center_y": 883.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 573,
        "bottom": 602,
        "center_x": 996.0,
        "center_y": 587.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 928,
        "bottom": 958,
        "center_x": 542.0,
        "center_y": 943.0,
        "text": "25"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1341,
        "bottom": 1370,
        "center_x": 316.0,
        "center_y": 1355.5,
        "text": "5. 现金流量套期储备"
      },
      {
        "left": 567,
        "right": 870,
        "top": 898,
        "bottom": 928,
        "center_x": 718.5,
        "center_y": 913.0,
        "text": "-4,268,794.07"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 602,
        "bottom": 632,
        "center_x": 996.0,
        "center_y": 617.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 958,
        "bottom": 987,
        "center_x": 542.0,
        "center_y": 972.5,
        "text": "26"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1370,
        "bottom": 1399,
        "center_x": 316.0,
        "center_y": 1384.5,
        "text": "6. 外币财务报表折算差额"
      },
      {
        "left": 567,
        "right": 870,
        "top": 928,
        "bottom": 958,
        "center_x": 718.5,
        "center_y": 943.0,
        "text": "-4,268,794.07"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 632,
        "bottom": 662,
        "center_x": 996.0,
        "center_y": 647.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 987,
        "bottom": 1016,
        "center_x": 542.0,
        "center_y": 1001.5,
        "text": "27"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1399,
        "bottom": 1428,
        "center_x": 316.0,
        "center_y": 1413.5,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 958,
        "bottom": 987,
        "center_x": 718.5,
        "center_y": 972.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 662,
        "bottom": 691,
        "center_x": 996.0,
        "center_y": 676.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1016,
        "bottom": 1046,
        "center_x": 542.0,
        "center_y": 1031.0,
        "text": "28"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1428,
        "bottom": 1457,
        "center_x": 316.0,
        "center_y": 1442.5,
        "text": "六、综合收益总额"
      },
      {
        "left": 567,
        "right": 870,
        "top": 987,
        "bottom": 1016,
        "center_x": 718.5,
        "center_y": 1001.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 691,
        "bottom": 721,
        "center_x": 996.0,
        "center_y": 706.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1046,
        "bottom": 1075,
        "center_x": 542.0,
        "center_y": 1060.5,
        "text": "29"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1457,
        "bottom": 1486,
        "center_x": 316.0,
        "center_y": 1471.5,
        "text": "七、每股收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1016,
        "bottom": 1046,
        "center_x": 718.5,
        "center_y": 1031.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 721,
        "bottom": 751,
        "center_x": 996.0,
        "center_y": 736.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1075,
        "bottom": 1105,
        "center_x": 542.0,
        "center_y": 1090.0,
        "text": "30"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1486,
        "bottom": 1514,
        "center_x": 316.0,
        "center_y": 1500.0,
        "text": "（一）基本每股收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1046,
        "bottom": 1075,
        "center_x": 718.5,
        "center_y": 1060.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 751,
        "bottom": 780,
        "center_x": 996.0,
        "center_y": 765.5,
        "text": "-4,131,163.60"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1105,
        "bottom": 1134,
        "center_x": 542.0,
        "center_y": 1119.5,
        "text": "31"
      },
      {
        "left": 115,
        "right": 517,
        "top": 1514,
        "bottom": 1544,
        "center_x": 316.0,
        "center_y": 1529.0,
        "text": "（二）稀释每股收益"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1075,
        "bottom": 1105,
        "center_x": 718.5,
        "center_y": 1090.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 780,
        "bottom": 809,
        "center_x": 996.0,
        "center_y": 794.5,
        "text": "2,360,293.77"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1134,
        "bottom": 1164,
        "center_x": 542.0,
        "center_y": 1149.0,
        "text": "32"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1105,
        "bottom": 1134,
        "center_x": 718.5,
        "center_y": 1119.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 809,
        "bottom": 839,
        "center_x": 996.0,
        "center_y": 824.0,
        "text": "83,187.95"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1164,
        "bottom": 1194,
        "center_x": 542.0,
        "center_y": 1179.0,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 1134,
        "bottom": 1164,
        "center_x": 718.5,
        "center_y": 1149.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 839,
        "bottom": 868,
        "center_x": 996.0,
        "center_y": 853.5,
        "text": "-1,854,057.78"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1194,
        "bottom": 1223,
        "center_x": 542.0,
        "center_y": 1208.5,
        "text": "33"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1164,
        "bottom": 1194,
        "center_x": 718.5,
        "center_y": 1179.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 868,
        "bottom": 898,
        "center_x": 996.0,
        "center_y": 883.0,
        "text": "539,316.23"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1223,
        "bottom": 1253,
        "center_x": 542.0,
        "center_y": 1238.0,
        "text": "34"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1194,
        "bottom": 1223,
        "center_x": 718.5,
        "center_y": 1208.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 898,
        "bottom": 928,
        "center_x": 996.0,
        "center_y": 913.0,
        "text": "-2,393,374.01"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1253,
        "bottom": 1281,
        "center_x": 542.0,
        "center_y": 1267.0,
        "text": "35"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1223,
        "bottom": 1253,
        "center_x": 718.5,
        "center_y": 1238.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 928,
        "bottom": 958,
        "center_x": 996.0,
        "center_y": 943.0,
        "text": "-2,393,374.01"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1281,
        "bottom": 1311,
        "center_x": 542.0,
        "center_y": 1296.0,
        "text": "36"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1253,
        "bottom": 1281,
        "center_x": 718.5,
        "center_y": 1267.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 958,
        "bottom": 987,
        "center_x": 996.0,
        "center_y": 972.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1311,
        "bottom": 1341,
        "center_x": 542.0,
        "center_y": 1326.0,
        "text": "37"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1281,
        "bottom": 1311,
        "center_x": 718.5,
        "center_y": 1296.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 987,
        "bottom": 1016,
        "center_x": 996.0,
        "center_y": 1001.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1341,
        "bottom": 1370,
        "center_x": 542.0,
        "center_y": 1355.5,
        "text": "38"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1311,
        "bottom": 1341,
        "center_x": 718.5,
        "center_y": 1326.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1016,
        "bottom": 1046,
        "center_x": 996.0,
        "center_y": 1031.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1370,
        "bottom": 1399,
        "center_x": 542.0,
        "center_y": 1384.5,
        "text": "39"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1341,
        "bottom": 1370,
        "center_x": 718.5,
        "center_y": 1355.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1046,
        "bottom": 1075,
        "center_x": 996.0,
        "center_y": 1060.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1399,
        "bottom": 1428,
        "center_x": 542.0,
        "center_y": 1413.5,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 1370,
        "bottom": 1399,
        "center_x": 718.5,
        "center_y": 1384.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1075,
        "bottom": 1105,
        "center_x": 996.0,
        "center_y": 1090.0,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1428,
        "bottom": 1457,
        "center_x": 542.0,
        "center_y": 1442.5,
        "text": "40"
      },
      {
        "left": 567,
        "right": 870,
        "top": 1399,
        "bottom": 1428,
        "center_x": 718.5,
        "center_y": 1413.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1457,
        "bottom": 1486,
        "center_x": 542.0,
        "center_y": 1471.5,
        "text": "41"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1105,
        "bottom": 1134,
        "center_x": 996.0,
        "center_y": 1119.5,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 1428,
        "bottom": 1457,
        "center_x": 718.5,
        "center_y": 1442.5,
        "text": "-4,268,794.07"
      },
      {
        "left": 517,
        "right": 567,
        "top": 1486,
        "bottom": 1514,
        "center_x": 542.0,
        "center_y": 1500.0,
        "text": "42"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1134,
        "bottom": 1164,
        "center_x": 996.0,
        "center_y": 1149.0,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 1457,
        "bottom": 1486,
        "center_x": 718.5,
        "center_y": 1471.5,
        "text": ""
      },
      {
        "left": 517,
        "right": 567,
        "top": 1514,
        "bottom": 1544,
        "center_x": 542.0,
        "center_y": 1529.0,
        "text": "43"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1164,
        "bottom": 1194,
        "center_x": 996.0,
        "center_y": 1179.0,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 1486,
        "bottom": 1514,
        "center_x": 718.5,
        "center_y": 1500.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1194,
        "bottom": 1223,
        "center_x": 996.0,
        "center_y": 1208.5,
        "text": ""
      },
      {
        "left": 567,
        "right": 870,
        "top": 1514,
        "bottom": 1544,
        "center_x": 718.5,
        "center_y": 1529.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1223,
        "bottom": 1253,
        "center_x": 996.0,
        "center_y": 1238.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1253,
        "bottom": 1281,
        "center_x": 996.0,
        "center_y": 1267.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1281,
        "bottom": 1311,
        "center_x": 996.0,
        "center_y": 1296.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1311,
        "bottom": 1341,
        "center_x": 996.0,
        "center_y": 1326.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1341,
        "bottom": 1370,
        "center_x": 996.0,
        "center_y": 1355.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1370,
        "bottom": 1399,
        "center_x": 996.0,
        "center_y": 1384.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1399,
        "bottom": 1428,
        "center_x": 996.0,
        "center_y": 1413.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1428,
        "bottom": 1457,
        "center_x": 996.0,
        "center_y": 1442.5,
        "text": "-2,393,374.01"
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1457,
        "bottom": 1486,
        "center_x": 996.0,
        "center_y": 1471.5,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1486,
        "bottom": 1514,
        "center_x": 996.0,
        "center_y": 1500.0,
        "text": ""
      },
      {
        "left": 870,
        "right": 1122,
        "top": 1514,
        "bottom": 1544,
        "center_x": 996.0,
        "center_y": 1529.0,
        "text": "0、"
      }
    ],
    "range": {
      "left": 115,
      "right": 1122,
      "top": 190,
      "bottom": 1544,
      "center_x": 618.5,
      "center_y": 867.0
    },
    "text": "项目 一、营业收入 减：营业成本 税金及附加 销售费用 管理费用 研发费用 财务费用 其中：利息费用 利息收入 加：其他收益 投资收益（损失以“-”号填列) 其中：对联营企业和合营企业的投资收益 以摊余成本计量的金融资产终止确认收益 行次 净敞口套期收益（损失以“-”号填列） 1 公允价值变动收益（损失以“-”号填列） 本期数 2 信用减值损失（损失以“-”号填列) 12,300,846.24 3 资产减值损失（损失以“-”号填列)  4 资产处置收益（损失以“-”号填列）  5 二、营业利润（亏损以“-”号填列）  6 加：营业外收入 2,606,207.88 7 减：营业外支出  .11,359,680.41 8 三、利润总额（亏损总额以“-”号填列） 128,163.30 404,741.70 9 减：所得税费用 1,848,347.51 -10,775.80 10 四、净利润（净亏损以“-”号填列） 33,490.23 11 （一）持续经营净利润（净亏损以“-”号填列）  本年累计数 12 （二）终止经营净利润（净亏损以“-”号填列）  115,273,945.12 13 五、其他综合收益的税后净额   14 （一）不能重分类进损益的其他综合收益   15 1. 重新计量设定受益计划变动额   16 734,837.88 2.权益法下不能转损益的其他综合收益  19,807,751.68 17 20,007,546.08 3. 其他权益工具投资公允价值变动  77,546,764.72 95,948.24 18 4. 企业自身信用风险公允价值变动  1,652,097.24 19   -49,105.24 20 （二）将重分类进损益的其他综合收益 -4,046,294.56 52,829.65 21 1. 权益法下可转损益的其他综合收益 -146,250.47 218,203.71 22 2.其他债权投资公允价值变动 76,249.04 221,633.41 23 3. 金融资产重分类计入其他综合收益的金额 -4,268,794.07  24 4. 其他债权投资信用减值准备   25 5. 现金流量套期储备 -4,268,794.07  26 6. 外币财务报表折算差额 -4,268,794.07  27    28 六、综合收益总额   29 七、每股收益   30 （一）基本每股收益  -4,131,163.60 31 （二）稀释每股收益  2,360,293.77 32  83,187.95   -1,854,057.78 33  539,316.23 34  -2,393,374.01 35  -2,393,374.01 36   37   38   39      40  41  -4,268,794.07 42   43            -2,393,374.01   0、"
  },
  {
    "page_id": 4,
    "type": "table",
    "cells": [
      {
        "left": 517,
        "right": 649,
        "top": 1720,
        "bottom": 1795,
        "center_x": 583.0,
        "center_y": 1757.5,
        "text": ""
      },
      {
        "left": 649,
        "right": 980,
        "top": 1720,
        "bottom": 1795,
        "center_x": 814.5,
        "center_y": 1757.5,
        "text": ""
      },
      {
        "left": 980,
        "right": 1059,
        "top": 1720,
        "bottom": 1795,
        "center_x": 1019.5,
        "center_y": 1757.5,
        "text": ""
      }
    ],
    "range": {
      "left": 517,
      "right": 1059,
      "top": 1720,
      "bottom": 1795,
      "center_x": 788.0,
      "center_y": 1757.5
    },
    "text": "  "
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 654.8496362686783,
      "right": 1045.4899156334357,
      "top": 187.8386451259328,
      "bottom": 210.0484655968729,
      "center_x": 850.169775951057,
      "center_y": 198.94355536140284
    },
    "text": "、增值税纳税申报表（一般纳税人适用）"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 102.94041187243853,
      "right": 302.82240681337714,
      "top": 209.05709015701734,
      "bottom": 221.8670575679359,
      "center_x": 202.88140934290783,
      "center_y": 215.46207386247661
    },
    "text": "纳税人识别号：91320505MA1MAPMD8J"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 1319.8307280855927,
      "right": 1385.75722611247,
      "top": 214.60082880152348,
      "bottom": 227.36541566534484,
      "center_x": 1352.7939770990315,
      "center_y": 220.98312223343416
    },
    "text": "税款所属期："
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 1399.620103799509,
      "right": 1618.5247347798093,
      "top": 215.31076689071932,
      "bottom": 227.8996834266224,
      "center_x": 1509.0724192896591,
      "center_y": 221.60522515867086
    },
    "text": "2022年 12月 01日至 2022年 12月 31日"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 102.76266157466556,
      "right": 339.7990704081273,
      "top": 222.86822883508313,
      "bottom": 235.51422144980683,
      "center_x": 221.28086599139644,
      "center_y": 229.19122514244498
    },
    "text": "纳税人名称：苏州梅克兰循环科技有限公司"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 1429.6155263402288,
      "right": 1614.3659946569721,
      "top": 229.3263822124252,
      "bottom": 241.8048504371699,
      "center_x": 1521.9907604986006,
      "center_y": 235.56561632479753
    },
    "text": "金额单位：人民币元（列至角分）"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 95.89559308449182,
      "right": 146.60251000884966,
      "top": 756.3568320481837,
      "bottom": 769.3830233118715,
      "center_x": 121.24905154667074,
      "center_y": 762.8699276800276
    },
    "text": "附加税费"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 185.76917657026024,
      "right": 359.79591071979866,
      "top": 757.457612137606,
      "bottom": 769.7228624700839,
      "center_x": 272.7825436450295,
      "center_y": 763.590237303845
    },
    "text": "教育费附加本期应补（退）费额"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 533.5669401549268,
      "right": 545.1472836651435,
      "top": 745.9956196560313,
      "bottom": 758.9428486977504,
      "center_x": 539.3571119100352,
      "center_y": 752.4692341768908
    },
    "text": "39"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 186.15297916879936,
      "right": 384.7783576456528,
      "top": 744.9386664178182,
      "bottom": 757.4987634268612,
      "center_x": 285.4656684072261,
      "center_y": 751.2187149223397
    },
    "text": "城市维护建设税本期应补（退）税额"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 848.7728609501897,
      "right": 903.9760493297298,
      "top": 747.5768842010363,
      "bottom": 760.1289291072627,
      "center_x": 876.3744551399598,
      "center_y": 753.8529066541495
    },
    "text": "55,478,11"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 185.40957351241556,
      "right": 372.0043484847078,
      "top": 769.9127291950219,
      "bottom": 782.5799096677802,
      "center_x": 278.70696099856167,
      "center_y": 776.246319431401
    },
    "text": "地方教育附加本期应补（退）费额"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 533.4988513408468,
      "right": 545.3736544001848,
      "top": 758.7141710273542,
      "bottom": 771.9137106599987,
      "center_x": 539.4362528705158,
      "center_y": 765.3139408436764
    },
    "text": "40"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 1100.3657306256077,
      "right": 1161.4675776584118,
      "top": 748.8798271769933,
      "bottom": 761.4718347860066,
      "center_x": 1130.9166541420097,
      "center_y": 755.1758309815
    },
    "text": "385,465.39"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 848.8410874120063,
      "right": 873.6165004382635,
      "top": 760.0315167313925,
      "bottom": 772.694480807182,
      "center_x": 861.2287939251349,
      "center_y": 766.3629987692873
    },
    "text": "23,7"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 533.5459657948388,
      "right": 544.3102882340735,
      "top": 771.088769964804,
      "bottom": 783.8599167652392,
      "center_x": 538.9281270144561,
      "center_y": 777.4743433650216
    },
    "text": "41"
  },
  {
    "page_id": 5,
    "type": "text",
    "range": {
      "left": 849.253435250574,
      "right": 873.4475758792786,
      "top": 772.5169466494316,
      "bottom": 785.243535783498,
      "center_x": 861.3505055649263,
      "center_y": 778.8802412164648
    },
    "text": "15,8"
  },
  {
    "page_id": 5,
    "type": "table",
    "cells": [
      {
        "left": 9,
        "right": 59,
        "top": 242,
        "bottom": 304,
        "center_x": 34.0,
        "center_y": 273.0,
        "text": ""
      },
      {
        "left": 59,
        "right": 1658,
        "top": 242,
        "bottom": 264,
        "center_x": 858.5,
        "center_y": 253.0,
        "text": "项目 栏次 一般项目 本月数 即征即退项目 本年累计 本月数 本年累计"
      },
      {
        "left": 9,
        "right": 59,
        "top": 304,
        "bottom": 851,
        "center_x": 34.0,
        "center_y": 577.5,
        "text": ""
      },
      {
        "left": 59,
        "right": 1658,
        "top": 264,
        "bottom": 304,
        "center_x": 858.5,
        "center_y": 284.0,
        "text": "EC）按适用税率计税销售额 其中：应税货物销售额 1 12,234,820.38 5 77,202,307.2 2 11,144,223,72 0 35,198,794.44 应税劳务销售额 58,579,337.59 3 0 0 35,198,794.44 0 0 0"
      },
      {
        "left": 59,
        "right": 325,
        "top": 304,
        "bottom": 341,
        "center_x": 192.0,
        "center_y": 322.5,
        "text": "纳税检直调整的销售 销售额 （二）桉份易办法计税销 其中：纳税检査调整的销"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 341,
        "bottom": 391,
        "center_x": 858.5,
        "center_y": 366.0,
        "text": "（三）免二抵，退办法出口销售额 （四）免税销售碲工 7 0 其中，免税货物销售额 8 0 66,025.86 9 3,403,8I6.95 免税劳务悄售额 66,025.86 10 3,403,816,95 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 391,
        "bottom": 404,
        "center_x": 858.5,
        "center_y": 397.5,
        "text": "销项税额 11 1,526,835.24 8,839,175,3 0 4,575,843.33"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 404,
        "bottom": 416,
        "center_x": 858.5,
        "center_y": 410.0,
        "text": "汪项税额 12 745,869 5,188,199.97 0 2,342,478.2"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 416,
        "bottom": 428,
        "center_x": 858.5,
        "center_y": 422.0,
        "text": "上期留抵税额 13 0 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 428,
        "bottom": 439,
        "center_x": 858.5,
        "center_y": 433.5,
        "text": "进项税额转出 14 11,578.2 94,014.69 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 439,
        "bottom": 466,
        "center_x": 858.5,
        "center_y": 452.5,
        "text": "免、抵、退应退税额 15 按适用税率计算的纳税检查应补缴税额 0 50,207.38 16 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 466,
        "bottom": 486,
        "center_x": 858.5,
        "center_y": 476.0,
        "text": "税款计算 应抵扣税额合计 17=12+13-14-15+16 734,290.8 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 486,
        "bottom": 512,
        "center_x": 858.5,
        "center_y": 499.0,
        "text": "实际抵扣税额 18（如17<11，则为17，否则为11） 734,290.8 应纳税额 19=11-18 0 0 2,342,478.2 792,544,44 2,857,249.23 0 2,233,365.13"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 512,
        "bottom": 562,
        "center_x": 858.5,
        "center_y": 537.0,
        "text": "期末留抵税额 20=17-18 简易计税办法计算的应纳税额 0 21 0 0 按简易计税办法计算的纳税检查应补缴税额 0 22 0 0 应纳税额减征额 0 0 23 0 0 720 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 562,
        "bottom": 611,
        "center_x": 858.5,
        "center_y": 586.5,
        "text": "应纳税额合计 24=19+21-23 期初未缴税额（多缴为负数） 792,544.44 2,856,529,23 25 0 3,368,474.63 2,233,365.13 实收出口开真专用缴款书退税额 26 1,304,489.84 10,547,392.17 8,314,027.04 本舫已缴税额 0 27=28+29+30+31 0 0 0 0 0"
      },
      {
        "left": 325,
        "right": 1658,
        "top": 304,
        "bottom": 341,
        "center_x": 991.5,
        "center_y": 322.5,
        "text": "额 4 售额 0 5 0 0 哲额 0 0 6 0 0 0 0 0 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 611,
        "bottom": 672,
        "center_x": 858.5,
        "center_y": 641.5,
        "text": "①分次预缴税额 28 ②出口开具专用缴款书预缴税额 0 29 0 ③本期缴纳上期应纳税额 0 30 ④本期缴纳欠缴税额 0 0 0 0 税款缴纳 31 期末未缴税额（多缴为负数） 0 32=24+25+26-27 0 4,161,019.07 0 0 4,161,019.07 10,547,392.17 10,547,392.17"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 672,
        "bottom": 684,
        "center_x": 858.5,
        "center_y": 678.0,
        "text": "其中：欠缴税额（≥0） 33=25+26-27 3,368,474.63 10,547,392.17"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 684,
        "bottom": 697,
        "center_x": 858.5,
        "center_y": 690.5,
        "text": "本期应补（退)税额 34一24-28-29 792,544.44 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 697,
        "bottom": 749,
        "center_x": 858.5,
        "center_y": 723.0,
        "text": "即征即退实际退税额 35 期初未缴查补税额 36 0 本期入库查补税额 0 1,308,359.79 37 0 期末未缴查扑税额 0 38=16+22+36-37 0 0 0"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 786,
        "bottom": 800,
        "center_x": 858.5,
        "center_y": 793.0,
        "text": "受理信息"
      },
      {
        "left": 59,
        "right": 1658,
        "top": 800,
        "bottom": 851,
        "center_x": 858.5,
        "center_y": 825.5,
        "text": "是否代理申报 否 经办人员身份证件类別 经办人名称 胡丹丹 居民身份证 经办人员身份证件号码 经办人地址 华金路266号 代理机构名称 360426*率******2025 授权人 代理机构统一社会信用代码 接收日则 2023-1-13 声明人 丁*"
      },
      {
        "left": 872,
        "right": 1658,
        "top": 762,
        "bottom": 786,
        "center_x": 1265.0,
        "center_y": 774.0,
        "text": "76,33 165,199.45 50.89 110,132,95"
      }
    ],
    "range": {
      "left": 9,
      "right": 1658,
      "top": 242,
      "bottom": 851,
      "center_x": 833.5,
      "center_y": 546.5
    },
    "text": " 项目 栏次 一般项目 本月数 即征即退项目 本年累计 本月数 本年累计  EC）按适用税率计税销售额 其中：应税货物销售额 1 12,234,820.38 5 77,202,307.2 2 11,144,223,72 0 35,198,794.44 应税劳务销售额 58,579,337.59 3 0 0 35,198,794.44 0 0 0 纳税检直调整的销售 销售额 （二）桉份易办法计税销 其中：纳税检査调整的销 （三）免二抵，退办法出口销售额 （四）免税销售碲工 7 0 其中，免税货物销售额 8 0 66,025.86 9 3,403,8I6.95 免税劳务悄售额 66,025.86 10 3,403,816,95 0 0 销项税额 11 1,526,835.24 8,839,175,3 0 4,575,843.33 汪项税额 12 745,869 5,188,199.97 0 2,342,478.2 上期留抵税额 13 0 0 0 进项税额转出 14 11,578.2 94,014.69 0 0 免、抵、退应退税额 15 按适用税率计算的纳税检查应补缴税额 0 50,207.38 16 0 0 税款计算 应抵扣税额合计 17=12+13-14-15+16 734,290.8 0 实际抵扣税额 18（如17<11，则为17，否则为11） 734,290.8 应纳税额 19=11-18 0 0 2,342,478.2 792,544,44 2,857,249.23 0 2,233,365.13 期末留抵税额 20=17-18 简易计税办法计算的应纳税额 0 21 0 0 按简易计税办法计算的纳税检查应补缴税额 0 22 0 0 应纳税额减征额 0 0 23 0 0 720 0 0 应纳税额合计 24=19+21-23 期初未缴税额（多缴为负数） 792,544.44 2,856,529,23 25 0 3,368,474.63 2,233,365.13 实收出口开真专用缴款书退税额 26 1,304,489.84 10,547,392.17 8,314,027.04 本舫已缴税额 0 27=28+29+30+31 0 0 0 0 0 额 4 售额 0 5 0 0 哲额 0 0 6 0 0 0 0 0 0 0 ①分次预缴税额 28 ②出口开具专用缴款书预缴税额 0 29 0 ③本期缴纳上期应纳税额 0 30 ④本期缴纳欠缴税额 0 0 0 0 税款缴纳 31 期末未缴税额（多缴为负数） 0 32=24+25+26-27 0 4,161,019.07 0 0 4,161,019.07 10,547,392.17 10,547,392.17 其中：欠缴税额（≥0） 33=25+26-27 3,368,474.63 10,547,392.17 本期应补（退)税额 34一24-28-29 792,544.44 0 即征即退实际退税额 35 期初未缴查补税额 36 0 本期入库查补税额 0 1,308,359.79 37 0 期末未缴查扑税额 0 38=16+22+36-37 0 0 0 受理信息 是否代理申报 否 经办人员身份证件类別 经办人名称 胡丹丹 居民身份证 经办人员身份证件号码 经办人地址 华金路266号 代理机构名称 360426*率******2025 授权人 代理机构统一社会信用代码 接收日则 2023-1-13 声明人 丁* 76,33 165,199.45 50.89 110,132,95"
  }
]

res_json = {}
res_list = []
page_id = 1
for o in range(len(edcut)+1):
    res_json[str(o)] = ''
for o in ocr_res:
    res_json[str(o['page_id'])] += o['text'].strip().replace(' ', '')
    text = res_json[str(o['page_id'])]
    time = ''
    if re.search(r"(20\d{2}-\d{1,2})", text):
        time += re.search(r"(20\d{2}-\d{1,2})", text).group(0)
    elif re.search(r"(20\d{2}年\d{1,2})", text):
        time += re.search(r"(20\d{2}年\d{1,2})", text).group(0).replace('年', '-')
    else:
        time = ''
    res_json[str(o['page_id'])] = time
for r in res_json.keys():
    res_list.append(res_json[r])

print(len(res_list))
print(res_json)
print(len(edcut))
cur = ''
for i in range(len(res_list)):
    if res_list[i] != '':
        cur = res_list[i]
    else:
        res_list[i] = cur

for i in range(len(edcut)):
    edcut[i]['result'] += " "
    edcut[i]['result'] += res_list[i]
print(edcut)
