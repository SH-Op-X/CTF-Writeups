"use strict";

const { Mutex, sleep, Recurse, TaskManager, ProcessTask, ProcessTaskSequence, Solver, callImmediate, callSetTimeout, callNextTick, callReadFileSync } = require('./Util.js');
const fs = require('node:fs');
const mutex = [new Mutex(1), new Mutex(3)];
console.log = (...args) => {fs.writeFileSync(1, `${args}\n`)};

function manageTasks(execute) {
    function taskHandler(taskId, action) {
        if (taskId < 2304)
            return ProcessTask(taskId, action, (a) => { return execute(taskId + 1, a); })
        else {
            return ProcessTaskSequence(action,
                (id, i, completeTask) => {
                    return TaskManager((r) => {
                        return async (i, obj) => {
                            let idx = (id % 8) ? 0 : 1;
                            switch (i) {
                                case 0:
                                    await callReadFileSync(obj, mutex[idx], id);
                                    break;
                                case 1:
                                    callSetTimeout(obj, mutex[idx]);
                                    callImmediate(obj, mutex[idx]);
                                    break;
                                case 2:
                                    callNextTick(obj);
                                    obj.data ^= ((obj.data >> 6) | (obj.data << 2));
                                    break;
                                default:
                                    return completeTask(obj);
                            }
                            await sleep(0);
                            return r(i + 1,obj);
                        }})(0, { data: id });
                },
                (action) => {
                    return ProcessTask(3895813, null,
                        (task) => ProcessTask(3893664, task,
                        (task) => ProcessTask(3895583, task,
                        (task) => ProcessTask(3893639, task,
                        (task) => ProcessTask(3919755, task,
                        (task) => ProcessTask(3893694, task,
                        (task) => ProcessTask(3871506, task,
                        (task) => ProcessTask(3871544, task,
                        (task) => ProcessTask(3810527, task,
                        (task) => ProcessTask(3921672, task,
                        (task) => ProcessTask(3913158, task,
                        (task) => ProcessTask(3813122, task,
                        (task) => ProcessTask(3869603, task,
                        (task) => ProcessTask(3813209, task,
                        (task) => ProcessTask(3910936, task,
                        (task) => ProcessTask(3911023, task,
                        (task) => ProcessTask(3896081, task,
                        (task) => ProcessTask(3822626, task,
                        (task) => ProcessTask(3913160, task,
                        (task) => ProcessTask(3919793, task,
                        (task) => ProcessTask(3822653, task,
                        (task) => ProcessTask(3895614, task,
                        (task) => ProcessTask(3820987, task,
                        (task) => ProcessTask(3820987, task,
                        (task) => ProcessTask(3932159, task,
                        (task) => ProcessTask(3911025, task,
                        (task) => ProcessTask(3893657, task,
                        (task) => ProcessTask(3921671, task,
                        (task) => ProcessTask(3820578, task,
                        (task) => ProcessTask(3921709, task,
                        (task) => ProcessTask(3921698, task,
                        (task) => ProcessTask(3910918, task, (task) => Solver(task, action, (flag) => { console.log(`flag: ${flag}`); })
                    ))))))))))))))))))))))))))))))));
                }
            );
        }
    }
    return taskHandler;
}

TaskManager(manageTasks)(0, null);
