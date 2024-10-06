// lib: , url: package:babyapk/main.dart

// class id: 1048593, size: 0x8
class :: {

  static _ main(/* No info */) async {
    // ** addr: 0x3be02c, size: 0x48
    // 0x3be02c: EnterFrame
    //     0x3be02c: stp             fp, lr, [SP, #-0x10]!
    //     0x3be030: mov             fp, SP
    // 0x3be034: AllocStack(0x10)
    //     0x3be034: sub             SP, SP, #0x10
    // 0x3be038: SetupParameters()
    //     0x3be038: stur            NULL, [fp, #-8]
    // 0x3be03c: CheckStackOverflow
    //     0x3be03c: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x3be040: cmp             SP, x16
    //     0x3be044: b.ls            #0x3be06c
    // 0x3be048: InitAsync() -> Future<void?>
    //     0x3be048: ldr             x0, [PP, #0x300]  ; [pp+0x300] TypeArguments: <void?>
    //     0x3be04c: bl              #0x1a3688
    // 0x3be050: r0 = init()
    //     0x3be050: bl              #0x3d6be8  ; [package:babyapk/src/rust/frb_generated.dart] RustLib::init
    // 0x3be054: mov             x1, x0
    // 0x3be058: stur            x1, [fp, #-0x10]
    // 0x3be05c: r0 = Await()
    //     0x3be05c: bl              #0x1a3224  ; AwaitStub
    // 0x3be060: r0 = runApp()
    //     0x3be060: bl              #0x3be074  ; [package:flutter/src/widgets/binding.dart] ::runApp
    // 0x3be064: r0 = Null
    //     0x3be064: mov             x0, NULL
    // 0x3be068: r0 = ReturnAsyncNotFuture()
    //     0x3be068: b               #0x1a3000  ; ReturnAsyncNotFutureStub
    // 0x3be06c: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x3be06c: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x3be070: b               #0x3be048
  }
  [closure] static Future<void> main(dynamic) {
    // ** addr: 0x3d8a10, size: 0x2c
    // 0x3d8a10: EnterFrame
    //     0x3d8a10: stp             fp, lr, [SP, #-0x10]!
    //     0x3d8a14: mov             fp, SP
    // 0x3d8a18: CheckStackOverflow
    //     0x3d8a18: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x3d8a1c: cmp             SP, x16
    //     0x3d8a20: b.ls            #0x3d8a34
    // 0x3d8a24: r0 = main()
    //     0x3d8a24: bl              #0x3be02c  ; [package:babyapk/main.dart] ::main
    // 0x3d8a28: LeaveFrame
    //     0x3d8a28: mov             SP, fp
    //     0x3d8a2c: ldp             fp, lr, [SP], #0x10
    // 0x3d8a30: ret
    //     0x3d8a30: ret             
    // 0x3d8a34: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x3d8a34: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x3d8a38: b               #0x3d8a24
  }
}

// class id: 1581, size: 0x18, field offset: 0x14
class _MyHomePageState extends State<dynamic> {

  _ build(/* No info */) {
    // ** addr: 0x264788, size: 0x2d4
    // 0x264788: EnterFrame
    //     0x264788: stp             fp, lr, [SP, #-0x10]!
    //     0x26478c: mov             fp, SP
    // 0x264790: AllocStack(0x20)
    //     0x264790: sub             SP, SP, #0x20
    // 0x264794: SetupParameters(_MyHomePageState this /* r1 => r2, fp-0x8 */, dynamic _ /* r2 => r1 */)
    //     0x264794: stur            x1, [fp, #-8]
    //     0x264798: mov             x16, x2
    //     0x26479c: mov             x2, x1
    //     0x2647a0: mov             x1, x16
    // 0x2647a4: CheckStackOverflow
    //     0x2647a4: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x2647a8: cmp             SP, x16
    //     0x2647ac: b.ls            #0x264a50
    // 0x2647b0: r0 = of()
    //     0x2647b0: bl              #0x1fe658  ; [package:flutter/src/material/theme.dart] Theme::of
    // 0x2647b4: LoadField: r1 = r0->field_3f
    //     0x2647b4: ldur            w1, [x0, #0x3f]
    // 0x2647b8: DecompressPointer r1
    //     0x2647b8: add             x1, x1, HEAP, lsl #32
    // 0x2647bc: LoadField: r0 = r1->field_bf
    //     0x2647bc: ldur            w0, [x1, #0xbf]
    // 0x2647c0: DecompressPointer r0
    //     0x2647c0: add             x0, x0, HEAP, lsl #32
    // 0x2647c4: cmp             w0, NULL
    // 0x2647c8: b.ne            #0x2647d4
    // 0x2647cc: LoadField: r0 = r1->field_f
    //     0x2647cc: ldur            w0, [x1, #0xf]
    // 0x2647d0: DecompressPointer r0
    //     0x2647d0: add             x0, x0, HEAP, lsl #32
    // 0x2647d4: ldur            x2, [fp, #-8]
    // 0x2647d8: stur            x0, [fp, #-0x10]
    // 0x2647dc: LoadField: r1 = r2->field_b
    //     0x2647dc: ldur            w1, [x2, #0xb]
    // 0x2647e0: DecompressPointer r1
    //     0x2647e0: add             x1, x1, HEAP, lsl #32
    // 0x2647e4: cmp             w1, NULL
    // 0x2647e8: b.eq            #0x264a58
    // 0x2647ec: r0 = Text()
    //     0x2647ec: bl              #0x264bc8  ; AllocateTextStub -> Text (size=0x4c)
    // 0x2647f0: mov             x1, x0
    // 0x2647f4: r0 = "This is a easy mobile"
    //     0x2647f4: add             x0, PP, #0xc, lsl #12  ; [pp+0xcf68] "This is a easy mobile"
    //     0x2647f8: ldr             x0, [x0, #0xf68]
    // 0x2647fc: stur            x1, [fp, #-0x18]
    // 0x264800: StoreField: r1->field_b = r0
    //     0x264800: stur            w0, [x1, #0xb]
    // 0x264804: r0 = AppBar()
    //     0x264804: bl              #0x264bbc  ; AllocateAppBarStub -> AppBar (size=0x84)
    // 0x264808: mov             x1, x0
    // 0x26480c: ldur            x2, [fp, #-0x10]
    // 0x264810: ldur            x3, [fp, #-0x18]
    // 0x264814: stur            x0, [fp, #-0x10]
    // 0x264818: r0 = AppBar()
    //     0x264818: bl              #0x264ac0  ; [package:flutter/src/material/app_bar.dart] AppBar::AppBar
    // 0x26481c: ldur            x2, [fp, #-8]
    // 0x264820: LoadField: r0 = r2->field_13
    //     0x264820: ldur            w0, [x2, #0x13]
    // 0x264824: DecompressPointer r0
    //     0x264824: add             x0, x0, HEAP, lsl #32
    // 0x264828: stur            x0, [fp, #-0x18]
    // 0x26482c: r0 = TextField()
    //     0x26482c: bl              #0x264aac  ; AllocateTextFieldStub -> TextField (size=0x118)
    // 0x264830: mov             x3, x0
    // 0x264834: r0 = EditableText
    //     0x264834: ldr             x0, [PP, #0x75c8]  ; [pp+0x75c8] Type: EditableText
    // 0x264838: stur            x3, [fp, #-0x20]
    // 0x26483c: StoreField: r3->field_f = r0
    //     0x26483c: stur            w0, [x3, #0xf]
    // 0x264840: ldur            x0, [fp, #-0x18]
    // 0x264844: StoreField: r3->field_13 = r0
    //     0x264844: stur            w0, [x3, #0x13]
    // 0x264848: r0 = Instance_InputDecoration
    //     0x264848: add             x0, PP, #0xc, lsl #12  ; [pp+0xcf70] Obj!InputDecoration@460781
    //     0x26484c: ldr             x0, [x0, #0xf70]
    // 0x264850: StoreField: r3->field_1b = r0
    //     0x264850: stur            w0, [x3, #0x1b]
    // 0x264854: r0 = Instance_TextCapitalization
    //     0x264854: ldr             x0, [PP, #0x7bb0]  ; [pp+0x7bb0] Obj!TextCapitalization@46bf31
    // 0x264858: StoreField: r3->field_27 = r0
    //     0x264858: stur            w0, [x3, #0x27]
    // 0x26485c: r0 = Instance_TextAlign
    //     0x26485c: ldr             x0, [PP, #0x5008]  ; [pp+0x5008] Obj!TextAlign@46d8d1
    // 0x264860: StoreField: r3->field_33 = r0
    //     0x264860: stur            w0, [x3, #0x33]
    // 0x264864: r0 = false
    //     0x264864: add             x0, NULL, #0x30  ; false
    // 0x264868: StoreField: r3->field_6f = r0
    //     0x264868: stur            w0, [x3, #0x6f]
    // 0x26486c: r4 = true
    //     0x26486c: add             x4, NULL, #0x20  ; true
    // 0x264870: StoreField: r3->field_3f = r4
    //     0x264870: stur            w4, [x3, #0x3f]
    // 0x264874: r1 = "•"
    //     0x264874: add             x1, PP, #0xc, lsl #12  ; [pp+0xcf78] "•"
    //     0x264878: ldr             x1, [x1, #0xf78]
    // 0x26487c: StoreField: r3->field_47 = r1
    //     0x26487c: stur            w1, [x3, #0x47]
    // 0x264880: StoreField: r3->field_4b = r0
    //     0x264880: stur            w0, [x3, #0x4b]
    // 0x264884: StoreField: r3->field_4f = r4
    //     0x264884: stur            w4, [x3, #0x4f]
    // 0x264888: StoreField: r3->field_5b = r4
    //     0x264888: stur            w4, [x3, #0x5b]
    // 0x26488c: r1 = 1
    //     0x26488c: movz            x1, #0x1
    // 0x264890: StoreField: r3->field_5f = r1
    //     0x264890: stur            x1, [x3, #0x5f]
    // 0x264894: StoreField: r3->field_6b = r0
    //     0x264894: stur            w0, [x3, #0x6b]
    // 0x264898: d0 = 2.000000
    //     0x264898: fmov            d0, #2.00000000
    // 0x26489c: StoreField: r3->field_9f = d0
    //     0x26489c: stur            d0, [x3, #0x9f]
    // 0x2648a0: r1 = Instance_BoxHeightStyle
    //     0x2648a0: ldr             x1, [PP, #0x51f8]  ; [pp+0x51f8] Obj!BoxHeightStyle@46d791
    // 0x2648a4: StoreField: r3->field_b7 = r1
    //     0x2648a4: stur            w1, [x3, #0xb7]
    // 0x2648a8: r1 = Instance_BoxWidthStyle
    //     0x2648a8: ldr             x1, [PP, #0x51f0]  ; [pp+0x51f0] Obj!BoxWidthStyle@46d771
    // 0x2648ac: StoreField: r3->field_bb = r1
    //     0x2648ac: stur            w1, [x3, #0xbb]
    // 0x2648b0: r1 = Instance_EdgeInsets
    //     0x2648b0: ldr             x1, [PP, #0x7690]  ; [pp+0x7690] Obj!EdgeInsets@460271
    // 0x2648b4: StoreField: r3->field_c3 = r1
    //     0x2648b4: stur            w1, [x3, #0xc3]
    // 0x2648b8: r1 = Instance_DragStartBehavior
    //     0x2648b8: ldr             x1, [PP, #0x75b8]  ; [pp+0x75b8] Obj!DragStartBehavior@46d211
    // 0x2648bc: StoreField: r3->field_cf = r1
    //     0x2648bc: stur            w1, [x3, #0xcf]
    // 0x2648c0: StoreField: r3->field_d7 = r0
    //     0x2648c0: stur            w0, [x3, #0xd7]
    // 0x2648c4: r1 = const []
    //     0x2648c4: ldr             x1, [PP, #0x7ba0]  ; [pp+0x7ba0] List<String>(0)
    // 0x2648c8: StoreField: r3->field_ef = r1
    //     0x2648c8: stur            w1, [x3, #0xef]
    // 0x2648cc: r1 = Instance_Clip
    //     0x2648cc: add             x1, PP, #0xb, lsl #12  ; [pp+0xbf08] Obj!Clip@46de31
    //     0x2648d0: ldr             x1, [x1, #0xf08]
    // 0x2648d4: StoreField: r3->field_f3 = r1
    //     0x2648d4: stur            w1, [x3, #0xf3]
    // 0x2648d8: StoreField: r3->field_fb = r4
    //     0x2648d8: stur            w4, [x3, #0xfb]
    // 0x2648dc: StoreField: r3->field_ff = r4
    //     0x2648dc: stur            w4, [x3, #0xff]
    // 0x2648e0: r1 = Closure: (BuildContext, EditableTextState) => Widget from Function '_defaultContextMenuBuilder@115181401': static.
    //     0x2648e0: ldr             x1, [PP, #0x7860]  ; [pp+0x7860] Closure: (BuildContext, EditableTextState) => Widget from Function '_defaultContextMenuBuilder@115181401': static. (0x2029362e068)
    // 0x2648e4: r17 = 263
    //     0x2648e4: movz            x17, #0x107
    // 0x2648e8: str             w1, [x3, x17]
    // 0x2648ec: r17 = 267
    //     0x2648ec: movz            x17, #0x10b
    // 0x2648f0: str             w4, [x3, x17]
    // 0x2648f4: r1 = Instance_SmartDashesType
    //     0x2648f4: ldr             x1, [PP, #0x7bb8]  ; [pp+0x7bb8] Obj!SmartDashesType@46c111
    // 0x2648f8: StoreField: r3->field_53 = r1
    //     0x2648f8: stur            w1, [x3, #0x53]
    // 0x2648fc: r1 = Instance_SmartQuotesType
    //     0x2648fc: add             x1, PP, #0xc, lsl #12  ; [pp+0xcf80] Obj!SmartQuotesType@46c0f1
    //     0x264900: ldr             x1, [x1, #0xf80]
    // 0x264904: StoreField: r3->field_57 = r1
    //     0x264904: stur            w1, [x3, #0x57]
    // 0x264908: r1 = Instance_TextInputType
    //     0x264908: add             x1, PP, #0xc, lsl #12  ; [pp+0xcf88] Obj!TextInputType@45fb91
    //     0x26490c: ldr             x1, [x1, #0xf88]
    // 0x264910: StoreField: r3->field_1f = r1
    //     0x264910: stur            w1, [x3, #0x1f]
    // 0x264914: StoreField: r3->field_c7 = r4
    //     0x264914: stur            w4, [x3, #0xc7]
    // 0x264918: ldur            x2, [fp, #-8]
    // 0x26491c: r1 = Function 'test':.
    //     0x26491c: add             x1, PP, #0xc, lsl #12  ; [pp+0xcf90] AnonymousClosure: (0x264bd4), in [package:babyapk/main.dart] _MyHomePageState::test (0x264c0c)
    //     0x264920: ldr             x1, [x1, #0xf90]
    // 0x264924: r0 = AllocateClosure()
    //     0x264924: bl              #0x3bb0a4  ; AllocateClosureStub
    // 0x264928: stur            x0, [fp, #-8]
    // 0x26492c: r0 = ElevatedButton()
    //     0x26492c: bl              #0x264aa0  ; AllocateElevatedButtonStub -> ElevatedButton (size=0x38)
    // 0x264930: mov             x3, x0
    // 0x264934: ldur            x0, [fp, #-8]
    // 0x264938: stur            x3, [fp, #-0x18]
    // 0x26493c: StoreField: r3->field_b = r0
    //     0x26493c: stur            w0, [x3, #0xb]
    // 0x264940: r0 = false
    //     0x264940: add             x0, NULL, #0x30  ; false
    // 0x264944: StoreField: r3->field_27 = r0
    //     0x264944: stur            w0, [x3, #0x27]
    // 0x264948: r4 = true
    //     0x264948: add             x4, NULL, #0x20  ; true
    // 0x26494c: StoreField: r3->field_2f = r4
    //     0x26494c: stur            w4, [x3, #0x2f]
    // 0x264950: r1 = Instance_Text
    //     0x264950: add             x1, PP, #0xc, lsl #12  ; [pp+0xcf98] Obj!Text@4693e1
    //     0x264954: ldr             x1, [x1, #0xf98]
    // 0x264958: StoreField: r3->field_33 = r1
    //     0x264958: stur            w1, [x3, #0x33]
    // 0x26495c: r1 = Null
    //     0x26495c: mov             x1, NULL
    // 0x264960: r2 = 4
    //     0x264960: movz            x2, #0x4
    // 0x264964: r0 = AllocateArray()
    //     0x264964: bl              #0x3bbd7c  ; AllocateArrayStub
    // 0x264968: mov             x2, x0
    // 0x26496c: ldur            x0, [fp, #-0x20]
    // 0x264970: stur            x2, [fp, #-8]
    // 0x264974: StoreField: r2->field_f = r0
    //     0x264974: stur            w0, [x2, #0xf]
    // 0x264978: ldur            x0, [fp, #-0x18]
    // 0x26497c: StoreField: r2->field_13 = r0
    //     0x26497c: stur            w0, [x2, #0x13]
    // 0x264980: r1 = <Widget>
    //     0x264980: ldr             x1, [PP, #0x59e8]  ; [pp+0x59e8] TypeArguments: <Widget>
    // 0x264984: r0 = AllocateGrowableArray()
    //     0x264984: bl              #0x3baca4  ; AllocateGrowableArrayStub
    // 0x264988: mov             x1, x0
    // 0x26498c: ldur            x0, [fp, #-8]
    // 0x264990: stur            x1, [fp, #-0x18]
    // 0x264994: StoreField: r1->field_f = r0
    //     0x264994: stur            w0, [x1, #0xf]
    // 0x264998: r0 = 4
    //     0x264998: movz            x0, #0x4
    // 0x26499c: StoreField: r1->field_b = r0
    //     0x26499c: stur            w0, [x1, #0xb]
    // 0x2649a0: r0 = Column()
    //     0x2649a0: bl              #0x264a94  ; AllocateColumnStub -> Column (size=0x30)
    // 0x2649a4: mov             x1, x0
    // 0x2649a8: r0 = Instance_Axis
    //     0x2649a8: add             x0, PP, #0xb, lsl #12  ; [pp+0xbea0] Obj!Axis@46cab1
    //     0x2649ac: ldr             x0, [x0, #0xea0]
    // 0x2649b0: stur            x1, [fp, #-8]
    // 0x2649b4: StoreField: r1->field_f = r0
    //     0x2649b4: stur            w0, [x1, #0xf]
    // 0x2649b8: r0 = Instance_MainAxisAlignment
    //     0x2649b8: add             x0, PP, #0xc, lsl #12  ; [pp+0xcfa0] Obj!MainAxisAlignment@46c771
    //     0x2649bc: ldr             x0, [x0, #0xfa0]
    // 0x2649c0: StoreField: r1->field_13 = r0
    //     0x2649c0: stur            w0, [x1, #0x13]
    // 0x2649c4: r0 = Instance_MainAxisSize
    //     0x2649c4: add             x0, PP, #0xc, lsl #12  ; [pp+0xcfa8] Obj!MainAxisSize@46c7d1
    //     0x2649c8: ldr             x0, [x0, #0xfa8]
    // 0x2649cc: StoreField: r1->field_17 = r0
    //     0x2649cc: stur            w0, [x1, #0x17]
    // 0x2649d0: r0 = Instance_CrossAxisAlignment
    //     0x2649d0: add             x0, PP, #0xb, lsl #12  ; [pp+0xbeb8] Obj!CrossAxisAlignment@46c691
    //     0x2649d4: ldr             x0, [x0, #0xeb8]
    // 0x2649d8: StoreField: r1->field_1b = r0
    //     0x2649d8: stur            w0, [x1, #0x1b]
    // 0x2649dc: r0 = Instance_VerticalDirection
    //     0x2649dc: add             x0, PP, #0xb, lsl #12  ; [pp+0xbec0] Obj!VerticalDirection@46ca71
    //     0x2649e0: ldr             x0, [x0, #0xec0]
    // 0x2649e4: StoreField: r1->field_23 = r0
    //     0x2649e4: stur            w0, [x1, #0x23]
    // 0x2649e8: r0 = Instance_Clip
    //     0x2649e8: add             x0, PP, #0xb, lsl #12  ; [pp+0xbc80] Obj!Clip@46ddf1
    //     0x2649ec: ldr             x0, [x0, #0xc80]
    // 0x2649f0: StoreField: r1->field_2b = r0
    //     0x2649f0: stur            w0, [x1, #0x2b]
    // 0x2649f4: ldur            x0, [fp, #-0x18]
    // 0x2649f8: StoreField: r1->field_b = r0
    //     0x2649f8: stur            w0, [x1, #0xb]
    // 0x2649fc: r0 = Center()
    //     0x2649fc: bl              #0x264a88  ; AllocateCenterStub -> Center (size=0x1c)
    // 0x264a00: mov             x1, x0
    // 0x264a04: r0 = Instance_Alignment
    //     0x264a04: add             x0, PP, #0xc, lsl #12  ; [pp+0xc3b0] Obj!Alignment@460681
    //     0x264a08: ldr             x0, [x0, #0x3b0]
    // 0x264a0c: stur            x1, [fp, #-0x18]
    // 0x264a10: StoreField: r1->field_f = r0
    //     0x264a10: stur            w0, [x1, #0xf]
    // 0x264a14: ldur            x0, [fp, #-8]
    // 0x264a18: StoreField: r1->field_b = r0
    //     0x264a18: stur            w0, [x1, #0xb]
    // 0x264a1c: r0 = Scaffold()
    //     0x264a1c: bl              #0x264a7c  ; AllocateScaffoldStub -> Scaffold (size=0x4c)
    // 0x264a20: ldur            x1, [fp, #-0x10]
    // 0x264a24: StoreField: r0->field_13 = r1
    //     0x264a24: stur            w1, [x0, #0x13]
    // 0x264a28: ldur            x1, [fp, #-0x18]
    // 0x264a2c: StoreField: r0->field_17 = r1
    //     0x264a2c: stur            w1, [x0, #0x17]
    // 0x264a30: r1 = true
    //     0x264a30: add             x1, NULL, #0x20  ; true
    // 0x264a34: StoreField: r0->field_43 = r1
    //     0x264a34: stur            w1, [x0, #0x43]
    // 0x264a38: r1 = false
    //     0x264a38: add             x1, NULL, #0x30  ; false
    // 0x264a3c: StoreField: r0->field_b = r1
    //     0x264a3c: stur            w1, [x0, #0xb]
    // 0x264a40: StoreField: r0->field_f = r1
    //     0x264a40: stur            w1, [x0, #0xf]
    // 0x264a44: LeaveFrame
    //     0x264a44: mov             SP, fp
    //     0x264a48: ldp             fp, lr, [SP], #0x10
    // 0x264a4c: ret
    //     0x264a4c: ret             
    // 0x264a50: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x264a50: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x264a54: b               #0x2647b0
    // 0x264a58: r0 = NullCastErrorSharedWithoutFPURegs()
    //     0x264a58: bl              #0x3bc42c  ; NullCastErrorSharedWithoutFPURegsStub
  }
  [closure] void test(dynamic) {
    // ** addr: 0x264bd4, size: 0x38
    // 0x264bd4: EnterFrame
    //     0x264bd4: stp             fp, lr, [SP, #-0x10]!
    //     0x264bd8: mov             fp, SP
    // 0x264bdc: ldr             x0, [fp, #0x10]
    // 0x264be0: LoadField: r1 = r0->field_17
    //     0x264be0: ldur            w1, [x0, #0x17]
    // 0x264be4: DecompressPointer r1
    //     0x264be4: add             x1, x1, HEAP, lsl #32
    // 0x264be8: CheckStackOverflow
    //     0x264be8: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x264bec: cmp             SP, x16
    //     0x264bf0: b.ls            #0x264c04
    // 0x264bf4: r0 = test()
    //     0x264bf4: bl              #0x264c0c  ; [package:babyapk/main.dart] _MyHomePageState::test
    // 0x264bf8: LeaveFrame
    //     0x264bf8: mov             SP, fp
    //     0x264bfc: ldp             fp, lr, [SP], #0x10
    // 0x264c00: ret
    //     0x264c00: ret             
    // 0x264c04: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x264c04: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x264c08: b               #0x264bf4
  }
  _ test(/* No info */) {
    // ** addr: 0x264c0c, size: 0x17c
    // 0x264c0c: EnterFrame
    //     0x264c0c: stp             fp, lr, [SP, #-0x10]!
    //     0x264c10: mov             fp, SP
    // 0x264c14: AllocStack(0x28)
    //     0x264c14: sub             SP, SP, #0x28
    // 0x264c18: CheckStackOverflow
    //     0x264c18: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x264c1c: cmp             SP, x16
    //     0x264c20: b.ls            #0x264d78
    // 0x264c24: LoadField: r0 = r1->field_13
    //     0x264c24: ldur            w0, [x1, #0x13]
    // 0x264c28: DecompressPointer r0
    //     0x264c28: add             x0, x0, HEAP, lsl #32
    // 0x264c2c: LoadField: r1 = r0->field_27
    //     0x264c2c: ldur            w1, [x0, #0x27]
    // 0x264c30: DecompressPointer r1
    //     0x264c30: add             x1, x1, HEAP, lsl #32
    // 0x264c34: LoadField: r0 = r1->field_7
    //     0x264c34: ldur            w0, [x1, #7]
    // 0x264c38: DecompressPointer r0
    //     0x264c38: add             x0, x0, HEAP, lsl #32
    // 0x264c3c: mov             x1, x0
    // 0x264c40: stur            x0, [fp, #-8]
    // 0x264c44: r2 = "ByteCTF{"
    //     0x264c44: add             x2, PP, #0xc, lsl #12  ; [pp+0xcfb0] "ByteCTF{"
    //     0x264c48: ldr             x2, [x2, #0xfb0]
    // 0x264c4c: r4 = const [0, 0x2, 0, 0x2, null]
    //     0x264c4c: ldr             x4, [PP, #0x170]  ; [pp+0x170] List(5) [0, 0x2, 0, 0x2, Null]
    // 0x264c50: r0 = startsWith()
    //     0x264c50: bl              #0x198d18  ; [dart:core] _StringBase::startsWith
    // 0x264c54: tbnz            w0, #4, #0x264d58
    // 0x264c58: ldur            x1, [fp, #-8]
    // 0x264c5c: LoadField: r0 = r1->field_7
    //     0x264c5c: ldur            w0, [x1, #7]
    // 0x264c60: r2 = LoadInt32Instr(r0)
    //     0x264c60: sbfx            x2, x0, #1, #0x1f
    // 0x264c64: stur            x2, [fp, #-0x10]
    // 0x264c68: sub             x0, x2, #1
    // 0x264c6c: lsl             x3, x0, #1
    // 0x264c70: stp             x3, x1, [SP, #8]
    // 0x264c74: r16 = "}"
    //     0x264c74: add             x16, PP, #8, lsl #12  ; [pp+0x8a40] "}"
    //     0x264c78: ldr             x16, [x16, #0xa40]
    // 0x264c7c: str             x16, [SP]
    // 0x264c80: r0 = _substringMatches()
    //     0x264c80: bl              #0x198df8  ; [dart:core] _StringBase::_substringMatches
    // 0x264c84: tbnz            w0, #4, #0x264d58
    // 0x264c88: ldur            x0, [fp, #-0x10]
    // 0x264c8c: cmp             x0, #0x2d
    // 0x264c90: b.ne            #0x264d58
    // 0x264c94: ldur            x1, [fp, #-8]
    // 0x264c98: r0 = LoadClassIdInstr(r1)
    //     0x264c98: ldur            x0, [x1, #-1]
    //     0x264c9c: ubfx            x0, x0, #0xc, #0x14
    // 0x264ca0: r2 = "{"
    //     0x264ca0: add             x2, PP, #8, lsl #12  ; [pp+0x8a18] "{"
    //     0x264ca4: ldr             x2, [x2, #0xa18]
    // 0x264ca8: r0 = GDT[cid_x0 + -0x1000]()
    //     0x264ca8: sub             lr, x0, #1, lsl #12
    //     0x264cac: ldr             lr, [x21, lr, lsl #3]
    //     0x264cb0: blr             lr
    // 0x264cb4: mov             x2, x0
    // 0x264cb8: LoadField: r0 = r2->field_b
    //     0x264cb8: ldur            w0, [x2, #0xb]
    // 0x264cbc: r1 = LoadInt32Instr(r0)
    //     0x264cbc: sbfx            x1, x0, #1, #0x1f
    // 0x264cc0: mov             x0, x1
    // 0x264cc4: r1 = 1
    //     0x264cc4: movz            x1, #0x1
    // 0x264cc8: cmp             x1, x0
    // 0x264ccc: b.hs            #0x264d80
    // 0x264cd0: LoadField: r0 = r2->field_f
    //     0x264cd0: ldur            w0, [x2, #0xf]
    // 0x264cd4: DecompressPointer r0
    //     0x264cd4: add             x0, x0, HEAP, lsl #32
    // 0x264cd8: LoadField: r1 = r0->field_13
    //     0x264cd8: ldur            w1, [x0, #0x13]
    // 0x264cdc: DecompressPointer r1
    //     0x264cdc: add             x1, x1, HEAP, lsl #32
    // 0x264ce0: r0 = LoadClassIdInstr(r1)
    //     0x264ce0: ldur            x0, [x1, #-1]
    //     0x264ce4: ubfx            x0, x0, #0xc, #0x14
    // 0x264ce8: r2 = "}"
    //     0x264ce8: add             x2, PP, #8, lsl #12  ; [pp+0x8a40] "}"
    //     0x264cec: ldr             x2, [x2, #0xa40]
    // 0x264cf0: r0 = GDT[cid_x0 + -0x1000]()
    //     0x264cf0: sub             lr, x0, #1, lsl #12
    //     0x264cf4: ldr             lr, [x21, lr, lsl #3]
    //     0x264cf8: blr             lr
    // 0x264cfc: mov             x2, x0
    // 0x264d00: LoadField: r0 = r2->field_b
    //     0x264d00: ldur            w0, [x2, #0xb]
    // 0x264d04: r1 = LoadInt32Instr(r0)
    //     0x264d04: sbfx            x1, x0, #1, #0x1f
    // 0x264d08: mov             x0, x1
    // 0x264d0c: r1 = 0
    //     0x264d0c: movz            x1, #0
    // 0x264d10: cmp             x1, x0
    // 0x264d14: b.hs            #0x264d84
    // 0x264d18: LoadField: r0 = r2->field_f
    //     0x264d18: ldur            w0, [x2, #0xf]
    // 0x264d1c: DecompressPointer r0
    //     0x264d1c: add             x0, x0, HEAP, lsl #32
    // 0x264d20: LoadField: r1 = r0->field_f
    //     0x264d20: ldur            w1, [x0, #0xf]
    // 0x264d24: DecompressPointer r1
    //     0x264d24: add             x1, x1, HEAP, lsl #32
    // 0x264d28: r0 = m3N4B5V6()
    //     0x264d28: bl              #0x265088  ; [package:babyapk/src/rust/api/simple.dart] ::m3N4B5V6
    // 0x264d2c: tbnz            w0, #4, #0x264d44
    // 0x264d30: r1 = "You Got it!!!!"
    //     0x264d30: add             x1, PP, #0xc, lsl #12  ; [pp+0xcfb8] "You Got it!!!!"
    //     0x264d34: ldr             x1, [x1, #0xfb8]
    // 0x264d38: r4 = const [0, 0x1, 0, 0x1, null]
    //     0x264d38: ldr             x4, [PP, #0x430]  ; [pp+0x430] List(5) [0, 0x1, 0, 0x1, Null]
    // 0x264d3c: r0 = showToast()
    //     0x264d3c: bl              #0x264d88  ; [package:fluttertoast/fluttertoast.dart] Fluttertoast::showToast
    // 0x264d40: b               #0x264d68
    // 0x264d44: r1 = "wrong flag"
    //     0x264d44: add             x1, PP, #0xc, lsl #12  ; [pp+0xcfc0] "wrong flag"
    //     0x264d48: ldr             x1, [x1, #0xfc0]
    // 0x264d4c: r4 = const [0, 0x1, 0, 0x1, null]
    //     0x264d4c: ldr             x4, [PP, #0x430]  ; [pp+0x430] List(5) [0, 0x1, 0, 0x1, Null]
    // 0x264d50: r0 = showToast()
    //     0x264d50: bl              #0x264d88  ; [package:fluttertoast/fluttertoast.dart] Fluttertoast::showToast
    // 0x264d54: b               #0x264d68
    // 0x264d58: r1 = "wrong flag"
    //     0x264d58: add             x1, PP, #0xc, lsl #12  ; [pp+0xcfc0] "wrong flag"
    //     0x264d5c: ldr             x1, [x1, #0xfc0]
    // 0x264d60: r4 = const [0, 0x1, 0, 0x1, null]
    //     0x264d60: ldr             x4, [PP, #0x430]  ; [pp+0x430] List(5) [0, 0x1, 0, 0x1, Null]
    // 0x264d64: r0 = showToast()
    //     0x264d64: bl              #0x264d88  ; [package:fluttertoast/fluttertoast.dart] Fluttertoast::showToast
    // 0x264d68: r0 = Null
    //     0x264d68: mov             x0, NULL
    // 0x264d6c: LeaveFrame
    //     0x264d6c: mov             SP, fp
    //     0x264d70: ldp             fp, lr, [SP], #0x10
    // 0x264d74: ret
    //     0x264d74: ret             
    // 0x264d78: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x264d78: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x264d7c: b               #0x264c24
    // 0x264d80: r0 = RangeErrorSharedWithoutFPURegs()
    //     0x264d80: bl              #0x3bc2cc  ; RangeErrorSharedWithoutFPURegsStub
    // 0x264d84: r0 = RangeErrorSharedWithoutFPURegs()
    //     0x264d84: bl              #0x3bc2cc  ; RangeErrorSharedWithoutFPURegsStub
  }
}

// class id: 1861, size: 0x10, field offset: 0xc
//   const constructor, 
class MyHomePage extends StatefulWidget {

  _OneByteString field_c;

  _ createState(/* No info */) {
    // ** addr: 0x2f9dd0, size: 0x94
    // 0x2f9dd0: EnterFrame
    //     0x2f9dd0: stp             fp, lr, [SP, #-0x10]!
    //     0x2f9dd4: mov             fp, SP
    // 0x2f9dd8: AllocStack(0x8)
    //     0x2f9dd8: sub             SP, SP, #8
    // 0x2f9ddc: CheckStackOverflow
    //     0x2f9ddc: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x2f9de0: cmp             SP, x16
    //     0x2f9de4: b.ls            #0x2f9e5c
    // 0x2f9de8: r1 = <TextEditingValue>
    //     0x2f9de8: ldr             x1, [PP, #0x7600]  ; [pp+0x7600] TypeArguments: <TextEditingValue>
    // 0x2f9dec: r0 = TextEditingController()
    //     0x2f9dec: bl              #0x2f9e70  ; AllocateTextEditingControllerStub -> TextEditingController (size=0x2c)
    // 0x2f9df0: mov             x1, x0
    // 0x2f9df4: r0 = Instance_TextEditingValue
    //     0x2f9df4: add             x0, PP, #0xc, lsl #12  ; [pp+0xc350] Obj!TextEditingValue@45fb51
    //     0x2f9df8: ldr             x0, [x0, #0x350]
    // 0x2f9dfc: stur            x1, [fp, #-8]
    // 0x2f9e00: StoreField: r1->field_27 = r0
    //     0x2f9e00: stur            w0, [x1, #0x27]
    // 0x2f9e04: r0 = 0
    //     0x2f9e04: movz            x0, #0
    // 0x2f9e08: StoreField: r1->field_7 = r0
    //     0x2f9e08: stur            x0, [x1, #7]
    // 0x2f9e0c: StoreField: r1->field_13 = r0
    //     0x2f9e0c: stur            x0, [x1, #0x13]
    // 0x2f9e10: StoreField: r1->field_1b = r0
    //     0x2f9e10: stur            x0, [x1, #0x1b]
    // 0x2f9e14: r0 = InitLateStaticField(0x538) // [package:flutter/src/foundation/change_notifier.dart] ChangeNotifier::_emptyListeners
    //     0x2f9e14: ldr             x0, [THR, #0x68]  ; THR::field_table_values
    //     0x2f9e18: ldr             x0, [x0, #0xa70]
    //     0x2f9e1c: ldr             x16, [PP, #0x40]  ; [pp+0x40] Sentinel
    //     0x2f9e20: cmp             w0, w16
    //     0x2f9e24: b.ne            #0x2f9e30
    //     0x2f9e28: ldr             x2, [PP, #0x2c68]  ; [pp+0x2c68] Field <ChangeNotifier._emptyListeners@228329750>: static late final (offset: 0x538)
    //     0x2f9e2c: bl              #0x3b9dc8
    // 0x2f9e30: mov             x1, x0
    // 0x2f9e34: ldur            x0, [fp, #-8]
    // 0x2f9e38: StoreField: r0->field_f = r1
    //     0x2f9e38: stur            w1, [x0, #0xf]
    // 0x2f9e3c: r1 = <MyHomePage>
    //     0x2f9e3c: add             x1, PP, #0xc, lsl #12  ; [pp+0xc358] TypeArguments: <MyHomePage>
    //     0x2f9e40: ldr             x1, [x1, #0x358]
    // 0x2f9e44: r0 = _MyHomePageState()
    //     0x2f9e44: bl              #0x2f9e64  ; Allocate_MyHomePageStateStub -> _MyHomePageState (size=0x18)
    // 0x2f9e48: ldur            x1, [fp, #-8]
    // 0x2f9e4c: StoreField: r0->field_13 = r1
    //     0x2f9e4c: stur            w1, [x0, #0x13]
    // 0x2f9e50: LeaveFrame
    //     0x2f9e50: mov             SP, fp
    //     0x2f9e54: ldp             fp, lr, [SP], #0x10
    // 0x2f9e58: ret
    //     0x2f9e58: ret             
    // 0x2f9e5c: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x2f9e5c: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x2f9e60: b               #0x2f9de8
  }
}

// class id: 1920, size: 0xc, field offset: 0xc
//   const constructor, 
class MyApp extends StatelessWidget {

  _ build(/* No info */) {
    // ** addr: 0x2fd3cc, size: 0xd8
    // 0x2fd3cc: EnterFrame
    //     0x2fd3cc: stp             fp, lr, [SP, #-0x10]!
    //     0x2fd3d0: mov             fp, SP
    // 0x2fd3d4: AllocStack(0x18)
    //     0x2fd3d4: sub             SP, SP, #0x18
    // 0x2fd3d8: CheckStackOverflow
    //     0x2fd3d8: ldr             x16, [THR, #0x38]  ; THR::stack_limit
    //     0x2fd3dc: cmp             SP, x16
    //     0x2fd3e0: b.ls            #0x2fd49c
    // 0x2fd3e4: r1 = Null
    //     0x2fd3e4: mov             x1, NULL
    // 0x2fd3e8: r2 = Instance_MaterialColor
    //     0x2fd3e8: add             x2, PP, #0xb, lsl #12  ; [pp+0xbda8] Obj!MaterialColor@46a4c1
    //     0x2fd3ec: ldr             x2, [x2, #0xda8]
    // 0x2fd3f0: r4 = const [0, 0x2, 0, 0x2, null]
    //     0x2fd3f0: ldr             x4, [PP, #0x170]  ; [pp+0x170] List(5) [0, 0x2, 0, 0x2, Null]
    // 0x2fd3f4: r0 = ColorScheme.fromSeed()
    //     0x2fd3f4: bl              #0x20431c  ; [package:flutter/src/material/color_scheme.dart] ColorScheme::ColorScheme.fromSeed
    // 0x2fd3f8: r16 = true
    //     0x2fd3f8: add             x16, NULL, #0x20  ; true
    // 0x2fd3fc: stp             x16, x0, [SP]
    // 0x2fd400: r1 = Null
    //     0x2fd400: mov             x1, NULL
    // 0x2fd404: r4 = const [0, 0x3, 0x2, 0x1, colorScheme, 0x1, useMaterial3, 0x2, null]
    //     0x2fd404: add             x4, PP, #0xb, lsl #12  ; [pp+0xbdb0] List(9) [0, 0x3, 0x2, 0x1, "colorScheme", 0x1, "useMaterial3", 0x2, Null]
    //     0x2fd408: ldr             x4, [x4, #0xdb0]
    // 0x2fd40c: r0 = ThemeData()
    //     0x2fd40c: bl              #0x200dd4  ; [package:flutter/src/material/theme_data.dart] ThemeData::ThemeData
    // 0x2fd410: stur            x0, [fp, #-8]
    // 0x2fd414: r0 = MaterialApp()
    //     0x2fd414: bl              #0x2fd4a4  ; AllocateMaterialAppStub -> MaterialApp (size=0x9c)
    // 0x2fd418: r1 = Instance_MyHomePage
    //     0x2fd418: add             x1, PP, #0xb, lsl #12  ; [pp+0xbdb8] Obj!MyHomePage@4693d1
    //     0x2fd41c: ldr             x1, [x1, #0xdb8]
    // 0x2fd420: StoreField: r0->field_13 = r1
    //     0x2fd420: stur            w1, [x0, #0x13]
    // 0x2fd424: r1 = _ConstMap len:0
    //     0x2fd424: add             x1, PP, #0xb, lsl #12  ; [pp+0xbdc0] Map<String, (dynamic this, BuildContext) => Widget>(0)
    //     0x2fd428: ldr             x1, [x1, #0xdc0]
    // 0x2fd42c: StoreField: r0->field_17 = r1
    //     0x2fd42c: stur            w1, [x0, #0x17]
    // 0x2fd430: r1 = const []
    //     0x2fd430: add             x1, PP, #0xb, lsl #12  ; [pp+0xbdc8] List<NavigatorObserver>(0)
    //     0x2fd434: ldr             x1, [x1, #0xdc8]
    // 0x2fd438: StoreField: r0->field_2f = r1
    //     0x2fd438: stur            w1, [x0, #0x2f]
    // 0x2fd43c: r1 = "Baby APK"
    //     0x2fd43c: add             x1, PP, #0xb, lsl #12  ; [pp+0xbdd0] "Baby APK"
    //     0x2fd440: ldr             x1, [x1, #0xdd0]
    // 0x2fd444: StoreField: r0->field_3f = r1
    //     0x2fd444: stur            w1, [x0, #0x3f]
    // 0x2fd448: ldur            x1, [fp, #-8]
    // 0x2fd44c: StoreField: r0->field_47 = r1
    //     0x2fd44c: stur            w1, [x0, #0x47]
    // 0x2fd450: r1 = Instance_ThemeMode
    //     0x2fd450: add             x1, PP, #0xb, lsl #12  ; [pp+0xbdd8] Obj!ThemeMode@46d0f1
    //     0x2fd454: ldr             x1, [x1, #0xdd8]
    // 0x2fd458: StoreField: r0->field_57 = r1
    //     0x2fd458: stur            w1, [x0, #0x57]
    // 0x2fd45c: r1 = Instance_Duration
    //     0x2fd45c: add             x1, PP, #0xb, lsl #12  ; [pp+0xbde0] Obj!Duration@46e0c1
    //     0x2fd460: ldr             x1, [x1, #0xde0]
    // 0x2fd464: StoreField: r0->field_5b = r1
    //     0x2fd464: stur            w1, [x0, #0x5b]
    // 0x2fd468: r1 = Instance__Linear
    //     0x2fd468: ldr             x1, [PP, #0x5630]  ; [pp+0x5630] Obj!_Linear@460ff1
    // 0x2fd46c: StoreField: r0->field_5f = r1
    //     0x2fd46c: stur            w1, [x0, #0x5f]
    // 0x2fd470: r1 = const [Instance of 'Locale']
    //     0x2fd470: add             x1, PP, #0xb, lsl #12  ; [pp+0xbde8] List<Locale>(1)
    //     0x2fd474: ldr             x1, [x1, #0xde8]
    // 0x2fd478: StoreField: r0->field_77 = r1
    //     0x2fd478: stur            w1, [x0, #0x77]
    // 0x2fd47c: r1 = false
    //     0x2fd47c: add             x1, NULL, #0x30  ; false
    // 0x2fd480: StoreField: r0->field_7b = r1
    //     0x2fd480: stur            w1, [x0, #0x7b]
    // 0x2fd484: StoreField: r0->field_7f = r1
    //     0x2fd484: stur            w1, [x0, #0x7f]
    // 0x2fd488: r1 = true
    //     0x2fd488: add             x1, NULL, #0x20  ; true
    // 0x2fd48c: StoreField: r0->field_83 = r1
    //     0x2fd48c: stur            w1, [x0, #0x83]
    // 0x2fd490: LeaveFrame
    //     0x2fd490: mov             SP, fp
    //     0x2fd494: ldp             fp, lr, [SP], #0x10
    // 0x2fd498: ret
    //     0x2fd498: ret             
    // 0x2fd49c: r0 = StackOverflowSharedWithoutFPURegs()
    //     0x2fd49c: bl              #0x3bbe84  ; StackOverflowSharedWithoutFPURegsStub
    // 0x2fd4a0: b               #0x2fd3e4
  }
}
