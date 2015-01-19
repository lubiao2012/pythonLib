import Queue

#三种队列可以选择
#python queue模块的FIFO队列先进先出
#class Queue.Queue(maxsize) FIFO
#LIFO类似于堆，即先进先出
#class Queue.LifoQueue(maxsize) LIFO
#还有一种是优先级队列级别越低越先出来
#class Queue.PriorityQueue(maxsize)  
#

#Queue.Queue 类是一个队列的同步实现，队列长度可以无限或者有限
#maxsize是可选参数，如果maxsize<1 ，则表示长度无限长度
myqueue = Queue.Queue(maxsize=10) 

#将一个值放入队列中
myqueue.put(10)

#从队头删除并返回一个项目。
myqueue.get()

#其他常见方法
#Queue.qsize() 返回队列的大小
#Queue.empty() 判断为空,真返回True
#Queue.full()
#Queue.task_done() 完成一项滞后，向任务已经完成的队列发送一个信号
#Queue.join() 实际上意味着等到队列为空，在执行别的操作，如果队列中存放的是线程，那么这个函数的作用是等待所有的线程全部都执行完成，一般是在多线程中使用到。