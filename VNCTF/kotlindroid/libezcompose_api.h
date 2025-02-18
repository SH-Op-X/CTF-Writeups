#ifndef KONAN_LIBEZCOMPOSE_H
#define KONAN_LIBEZCOMPOSE_H
#ifdef __cplusplus
extern "C" {
#endif
#ifdef __cplusplus
typedef bool            libezcompose_KBoolean;
#else
typedef _Bool           libezcompose_KBoolean;
#endif
typedef unsigned short     libezcompose_KChar;
typedef signed char        libezcompose_KByte;
typedef short              libezcompose_KShort;
typedef int                libezcompose_KInt;
typedef long long          libezcompose_KLong;
typedef unsigned char      libezcompose_KUByte;
typedef unsigned short     libezcompose_KUShort;
typedef unsigned int       libezcompose_KUInt;
typedef unsigned long long libezcompose_KULong;
typedef float              libezcompose_KFloat;
typedef double             libezcompose_KDouble;
typedef float __attribute__ ((__vector_size__ (16))) libezcompose_KVector128;
typedef void*              libezcompose_KNativePtr;
struct libezcompose_KType;
typedef struct libezcompose_KType libezcompose_KType;

typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Byte;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Short;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Int;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Long;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Float;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Double;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Char;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Boolean;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_Unit;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_UByte;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_UShort;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_UInt;
typedef struct {
  libezcompose_KNativePtr pinned;
} libezcompose_kref_kotlin_ULong;

extern libezcompose_KInt JNI_OnLoad(void* vm, void* preserved);
extern void* native_natget(void* env, void* thiz, void* byteArray);

typedef struct {
  /* Service functions. */
  void (*DisposeStablePointer)(libezcompose_KNativePtr ptr);
  void (*DisposeString)(const char* string);
  libezcompose_KBoolean (*IsInstance)(libezcompose_KNativePtr ref, const libezcompose_KType* type);
  libezcompose_kref_kotlin_Byte (*createNullableByte)(libezcompose_KByte);
  libezcompose_KByte (*getNonNullValueOfByte)(libezcompose_kref_kotlin_Byte);
  libezcompose_kref_kotlin_Short (*createNullableShort)(libezcompose_KShort);
  libezcompose_KShort (*getNonNullValueOfShort)(libezcompose_kref_kotlin_Short);
  libezcompose_kref_kotlin_Int (*createNullableInt)(libezcompose_KInt);
  libezcompose_KInt (*getNonNullValueOfInt)(libezcompose_kref_kotlin_Int);
  libezcompose_kref_kotlin_Long (*createNullableLong)(libezcompose_KLong);
  libezcompose_KLong (*getNonNullValueOfLong)(libezcompose_kref_kotlin_Long);
  libezcompose_kref_kotlin_Float (*createNullableFloat)(libezcompose_KFloat);
  libezcompose_KFloat (*getNonNullValueOfFloat)(libezcompose_kref_kotlin_Float);
  libezcompose_kref_kotlin_Double (*createNullableDouble)(libezcompose_KDouble);
  libezcompose_KDouble (*getNonNullValueOfDouble)(libezcompose_kref_kotlin_Double);
  libezcompose_kref_kotlin_Char (*createNullableChar)(libezcompose_KChar);
  libezcompose_KChar (*getNonNullValueOfChar)(libezcompose_kref_kotlin_Char);
  libezcompose_kref_kotlin_Boolean (*createNullableBoolean)(libezcompose_KBoolean);
  libezcompose_KBoolean (*getNonNullValueOfBoolean)(libezcompose_kref_kotlin_Boolean);
  libezcompose_kref_kotlin_Unit (*createNullableUnit)(void);
  libezcompose_kref_kotlin_UByte (*createNullableUByte)(libezcompose_KUByte);
  libezcompose_KUByte (*getNonNullValueOfUByte)(libezcompose_kref_kotlin_UByte);
  libezcompose_kref_kotlin_UShort (*createNullableUShort)(libezcompose_KUShort);
  libezcompose_KUShort (*getNonNullValueOfUShort)(libezcompose_kref_kotlin_UShort);
  libezcompose_kref_kotlin_UInt (*createNullableUInt)(libezcompose_KUInt);
  libezcompose_KUInt (*getNonNullValueOfUInt)(libezcompose_kref_kotlin_UInt);
  libezcompose_kref_kotlin_ULong (*createNullableULong)(libezcompose_KULong);
  libezcompose_KULong (*getNonNullValueOfULong)(libezcompose_kref_kotlin_ULong);

  /* User functions. */
  struct {
    struct {
      libezcompose_KInt (*JNI_OnLoad_)(void* vm, void* preserved);
      void* (*native_natget_)(void* env, void* thiz, void* byteArray);
    } root;
  } kotlin;
} libezcompose_ExportedSymbols;
extern libezcompose_ExportedSymbols* libezcompose_symbols(void);
#ifdef __cplusplus
}  /* extern "C" */
#endif
#endif  /* KONAN_LIBEZCOMPOSE_H */
