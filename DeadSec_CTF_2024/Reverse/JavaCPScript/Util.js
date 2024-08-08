"use strict";

const fs = require('node:fs');

class Mutex {
    constructor(version) {
        this._lock = Promise.resolve();

        const lock_v1 = () => {
            const q = this._lock.then(() => release);
            const release = this._acquire();
            return q;
        }
        const lock_v2 = () => {
            const release = this._acquire();
            return this._lock.then(() => release);
        }
        const lock_v3 = () => {
            return this._lock.then(() => this._acquire());
        }

        this.lock = () => {
            switch(version) {
                case 1:
                    return lock_v1();
                case 2:
                    return lock_v2();
                case 3:
                    return lock_v3();
                default:
                    console.error('version error');
            }
        }
    }
    _acquire() {
        let release;
        this._lock = new Promise(resolve => {
            release = resolve;
        })
        return release;
    }
}

function Recurse(fn) {
    return fn(fn);
}

function TaskManager(manager) {
    function CreateTask(task) {
        function ExecuteTask(...args) {
            return task(task)(...args);
        }
        return manager(ExecuteTask);
    }
    return Recurse(CreateTask);
}

function ProcessTask(id, action, next) {
    function RunTask(run) {
        return run(id, action);
    }
    return next(RunTask);
}

function ProcessTaskSequence(initialTask, processSubTask, onCompletion){
    function InitializeTaskProcessor(taskProcessor){
        function ExecuteTaskStep(currentTask, stepCount, nextStep){
            if (currentTask == null)
                return nextStep(null)
            else {
                function PrepareNextTask(subTask, taskContext) {
                    function SetupTaskContext(taskId){
                        function FinalizeTaskExecution(taskResult) {
                            return ProcessTask(taskId, taskResult, nextStep)
                        }
                        return taskProcessor(taskContext, stepCount + 1, FinalizeTaskExecution)
                    }
                    return processSubTask(subTask, stepCount, SetupTaskContext)
                }
                return currentTask(PrepareNextTask)
            }
        }
        return ExecuteTaskStep
    }
    return TaskManager(InitializeTaskProcessor)(initialTask, 0, onCompletion)
}

function Solver(a, b, c) {
    function S1(d) {
        function S2(e, f, g) {
            if ((e == null) || (f == null))
                return c(g)
            else {
                function S3(h, i) {
                    function S4(j, k) {
                         return d(i, k, (g) && ((h == null) ? true : (h == j.data)))
                    }
                    return f(S4)
                }
                return e(S3)
            }
        }
        return S2
    }
    return TaskManager(S1)(a, b, true)
}

async function callImmediate(obj, mutex) {
    setImmediate(async (...args) => {
        const [ release ] = args;
        obj.data ^= ((obj.data >> 7) | (obj.data << 1));
        release();
    }, await mutex.lock());
}
    
async function callSetTimeout(obj, mutex) {
    setTimeout(async (...args) => {
        const [release] = args;
        obj.data ^= ((obj.data >> 4) | (obj.data << 4));
        release();
    }, 0, await mutex.lock());
}
    
async function callNextTick(obj) {
    process.nextTick(() => {
        obj.data ^= ((obj.data >> 5) | (obj.data << 3));
    });
}
    
async function callReadFileSync(obj, mutex, range) {
    const release = await mutex.lock();
    const chunk = fs.readFileSync('input');
    obj.data ^= chunk[range%32];
    release();
}

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

module.exports = { Mutex, sleep, Recurse, TaskManager, ProcessTask, ProcessTaskSequence, Solver, callImmediate, callSetTimeout, callNextTick, callReadFileSync }
