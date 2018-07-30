---
title: "ConcurrentTimeRotatingFileHandler"

description: "并发(多进程, 多线程)写入日志, 并定时切割日志的python日志模块"

date: 2018-07-30 19:19:44

---


## 1 Introduction

This handler will write log events to log file which is rotated at special time. This module is based on ConcurrentLogHandler and TimedRotatingFileHandler. 


## 2 Requirement
注意, 该模块基于[ConcurrentLogHandler](https://pypi.org/project/ConcurrentLogHandler/)和``TimedRotatingFileHandler``进行构建.

其中对于多进程安全的逻辑完全仿照``ConcurrentLogHandler``的设计, 作为``TimeRotatingFileHandler``的子类, 结合两者, 实现了如下功能: 

+ 多进程, 多线程安全
+ 定时切割日志

注意, ``ConcurrentLogHanlder``中使用悲观文件锁机制来确保多进程安全, 该日志模块不适用于高并发的场景.


## 3 Environment
System: 目前代码仅仅支持在Linux, MacOS环境下执行, 暂未在Window上测试.

Python: 目前仅仅在py27上测试通过


## 4 Design
具体的模块设计思想或者思路, 见博客文章: [ConcurrentTimeRotatingFileHandler](https://unusebamboo.top/languages/python-logging-concurrent-time-rotating/)
