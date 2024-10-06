// lib: , url: package:babyapk/src/rust/api/simple.dart

// class id: 1048594, size: 0x8
class :: {

  static _ m3N4B5V6(/* No info */) {
    // ** addr: 0x265088, size: 0x98
    // 0x265088: EnterFrame
    //     0x265088: stp             fp, lr, [SP, #-0x10]!
    //     0x26508c: mov             fp, SP
    // 0x265090: AllocStack(0x8)
    //     0x265090: sub             SP, SP, #8
    // 0x265094: SetupParameters(dynamic _ /* r1 => r2, fp-0x8 */)
    //     0x265094: mov             x2, x1
    //     0x265098: stur            x1, [fp, #-8]
    // 0x26509c: CheckStackOverflow
    //     0x26509c: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x2650a0: cmp             SP, x16
    //     0x2650a4: b.ls            #0x265118
    // 0x2650a8: r0 = InitLateStaticField(0x4d8) // [package:babyapk/src/rust/frb_generated.dart] RustLib::instance
    //     0x2650a8: ldr             x0, [THR, #0x68]  ; THR::field_table_values
    //     0x2650ac: ldr             x0, [x0, #0x9b0]
    //     0x2650b0: ldr             x16, [PP, #0x40]  ; [pp+0x40] Sentinel
    //     0x2650b4: cmp             w0, w16
    //     0x2650b8: b.ne            #0x2650c8
    //     0x2650bc: add             x2, PP, #8, lsl #12  ; [pp+0x8278] Field <RustLib.instance>: static late final (offset: 0x4d8)
    //     0x2650c0: ldr             x2, [x2, #0x278]
    //     0x2650c4: bl              #0x3b9dc8
    // 0x2650c8: LoadField: r1 = r0->field_b
    //     0x2650c8: ldur            w1, [x0, #0xb]
    // 0x2650cc: DecompressPointer r1
    //     0x2650cc: add             x1, x1, HEAP, lsl #32
    // 0x2650d0: cmp             w1, NULL
    // 0x2650d4: b.eq            #0x2650f8
    // 0x2650d8: LoadField: r0 = r1->field_f
    //     0x2650d8: ldur            w0, [x1, #0xf]
    // 0x2650dc: DecompressPointer r0
    //     0x2650dc: add             x0, x0, HEAP, lsl #32
    // 0x2650e0: mov             x1, x0
    // 0x2650e4: ldur            x2, [fp, #-8]
    // 0x2650e8: r0 = crateApiSimpleM3N4B5V6()
    //     0x2650e8: bl              #0x26519c  ; [package:babyapk/src/rust/frb_generated.dart] RustLibApiImpl::crateApiSimpleM3N4B5V6
    // 0x2650ec: LeaveFrame
    //     0x2650ec: mov             SP, fp
    //     0x2650f0: ldp             fp, lr, [SP], #0x10
    // 0x2650f4: ret
    //     0x2650f4: ret             
    // 0x2650f8: r0 = StateError()
    //     0x2650f8: bl              #0x188914  ; AllocateStateErrorStub -> StateError (size=0x10)
    // 0x2650fc: mov             x1, x0
    // 0x265100: r0 = "flutter_rust_bridge has not been initialized. Did you forget to call `await RustLib.init();`\? (If you have configured a different lib name, change `RustLib` to your name.)"
    //     0x265100: add             x0, PP, #8, lsl #12  ; [pp+0x8420] "flutter_rust_bridge has not been initialized. Did you forget to call `await RustLib.init();`\? (If you have configured a different lib name, change `RustLib` to your name.)"
    //     0x265104: ldr             x0, [x0, #0x420]
    // 0x265108: StoreField: r1->field_b = r0
    //     0x265108: stur            w0, [x1, #0xb]
    // 0x26510c: mov             x0, x1
    // 0x265110: r0 = Throw()
    //     0x265110: bl              #0x3b9f2c  ; ThrowStub
    // 0x265114: brk             #0
    // 0x265118: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x265118: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x26511c: b               #0x2650a8
  }
}
