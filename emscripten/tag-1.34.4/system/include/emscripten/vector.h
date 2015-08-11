#ifndef __emscripten_vector_h__
#define __emscripten_vector_h__

#ifdef __cplusplus
extern "C" {
#endif

// Support for the JS SIMD API proposal, https://github.com/johnmccutchan/ecmascript_simd

typedef float float32x4 __attribute__((__vector_size__(16), __may_alias__));
typedef unsigned int int32x4 __attribute__((__vector_size__(16), __may_alias__));

unsigned int emscripten_float32x4_signmask(float32x4 __x) __attribute__((__nothrow__, __const__));

float32x4 emscripten_float32x4_min(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__));
float32x4 emscripten_float32x4_max(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__));
float32x4 emscripten_float32x4_abs(float32x4 __a) __attribute__((__nothrow__, __const__));
float32x4 emscripten_float32x4_sqrt(float32x4 __a) __attribute__((__nothrow__, __const__));
float32x4 emscripten_float32x4_reciprocalApproximation(float32x4 __a) __attribute__((__nothrow__, __const__));
float32x4 emscripten_float32x4_reciprocalSqrtApproximation(float32x4 __a) __attribute__((__nothrow__, __const__));
inline int32x4 emscripten_float32x4_lessThan(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__)) { return __a < __b; }
inline int32x4 emscripten_float32x4_lessThanOrEqual(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__)) { return __a <= __b; }
inline int32x4 emscripten_float32x4_equal(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__)) { return __a == __b; }
inline int32x4 emscripten_float32x4_notEqual(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__)) { return __a != __b; }
inline int32x4 emscripten_float32x4_greaterThanOrEqual(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__)) { return __a >= __b; }
inline int32x4 emscripten_float32x4_greaterThan(float32x4 __a, float32x4 __b) __attribute__((__nothrow__, __const__)) { return __a > __b; }
float32x4 emscripten_float32x4_select(int32x4 __a, float32x4 __b, float32x4 __c) __attribute__((__nothrow__, __const__));

inline int32x4 emscripten_int32x4_and(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a & __b; }
inline int32x4 emscripten_int32x4_or(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a | __b; }
inline int32x4 emscripten_int32x4_xor(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a ^ __b; }
inline int32x4 emscripten_int32x4_not(int32x4 __a) __attribute__((__nothrow__, __const__)) { return ~__a; }
inline int32x4 emscripten_int32x4_fromFloat32x4Bits(float32x4 __a) __attribute__((__nothrow__, __const__)) { return (int32x4)__a; }
inline int32x4 emscripten_int32x4_fromFloat32x4(float32x4 __a) __attribute__((__nothrow__, __const__)) { return __builtin_convertvector(__a, int32x4); }

inline int32x4 emscripten_int32x4_lessThan(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a < __b; }
inline int32x4 emscripten_int32x4_lessThanOrEqual(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a <= __b; }
inline int32x4 emscripten_int32x4_equal(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a == __b; }
inline int32x4 emscripten_int32x4_notEqual(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a != __b; }
inline int32x4 emscripten_int32x4_greaterThanOrEqual(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a >= __b; }
inline int32x4 emscripten_int32x4_greaterThan(int32x4 __a, int32x4 __b) __attribute__((__nothrow__, __const__)) { return __a > __b; }
int32x4 emscripten_int32x4_select(int32x4 __a, int32x4 __b, int32x4 __c) __attribute__((__nothrow__, __const__));

inline float32x4 emscripten_float32x4_fromInt32x4Bits(int32x4 __a) __attribute__((__nothrow__, __const__)) { return (float32x4)__a; }
inline float32x4 emscripten_float32x4_fromInt32x4(int32x4 __a) __attribute__((__nothrow__, __const__)) { return __builtin_convertvector(__a, float32x4); }

float32x4 emscripten_float32x4_load1(const void *__p) __attribute__((__nothrow__, __const__));
float32x4 emscripten_float32x4_load2(const void *__p) __attribute__((__nothrow__, __const__));
void emscripten_float32x4_store1(const void *__p, float32x4 __a) __attribute__((__nothrow__));
void emscripten_float32x4_store2(const void *__p, float32x4 __a) __attribute__((__nothrow__));

#ifdef __cplusplus
}
#endif

#endif