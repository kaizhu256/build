import os, shutil, logging, zlib

TAG = 'version_1'

def get(ports, settings, shared):
  if settings.USE_LIBPNG == 1:
    ports.fetch_project('libpng', 'https://github.com/emscripten-ports/libpng/archive/' + TAG + '.zip', 'libpng-' + TAG)
    def create():     
      zlib.get(ports, settings, shared);
      # TODO: clear dependent projects
      #ports.clear_project_build('sdl2-image')


      source_path = os.path.join(ports.get_dir(), 'libpng', 'libpng-' + TAG)
      dest_path = os.path.join(shared.Cache.get_path('ports-builds'), 'libpng')
      shared.try_delete(dest_path)
      os.makedirs(dest_path)
      shutil.rmtree(dest_path, ignore_errors=True)
      shutil.copytree(source_path, dest_path)
      open(os.path.join(dest_path, 'pnglibconf.h'), 'w').write(pnglibconf_h)

      # build
      srcs = 'png.c pngerror.c pngget.c pngmem.c pngpread.c pngread.c pngrio.c pngrtran.c pngrutil.c pngset.c pngtrans.c pngwio.c pngwrite.c pngwtran.c pngwutil.c'.split(' ')
      commands = []
      o_s = []
      for src in srcs:
        o = os.path.join(ports.get_build_dir(), 'libpng', src + '.o')
        shared.safe_ensure_dirs(os.path.dirname(o))
        commands.append([shared.PYTHON, shared.EMCC, os.path.join(dest_path, src), '-O2', '-o', o, '-I' + dest_path, '-s', 'USE_ZLIB=1',
                         '-Wno-warn-absolute-paths', '-w',])
        o_s.append(o)

      ports.run_commands(commands)
      final = os.path.join(ports.get_build_dir(), 'libpng', 'libpng.bc')
      shared.Building.link(o_s, final)
      return final
    return [shared.Cache.get('libpng', create, what='port')]
  else:
    return []


def process_args(ports, args, settings, shared):
  if settings.USE_LIBPNG == 1:
    get(ports, settings, shared)
    args += ['-Xclang', '-isystem' + os.path.join(shared.Cache.get_path('ports-builds'), 'libpng')]
  return args

def show():
  return 'libpng (USE_LIBPNG=1; zlib license)'

pnglibconf_h = r'''/* libpng 1.6.17 STANDARD API DEFINITION */

/* pnglibconf.h - library build configuration */

/* Libpng version 1.6.17 - March 26, 2015 */

/* Copyright (c) 1998-2014 Glenn Randers-Pehrson */

/* This code is released under the libpng license. */
/* For conditions of distribution and use, see the disclaimer */
/* and license in png.h */

/* pnglibconf.h */
/* Machine generated file: DO NOT EDIT */
/* Derived from: scripts/pnglibconf.dfa */
#ifndef PNGLCONF_H
#define PNGLCONF_H
/* options */
#define PNG_16BIT_SUPPORTED
#define PNG_ALIGNED_MEMORY_SUPPORTED
/*#undef PNG_ARM_NEON_API_SUPPORTED*/
/*#undef PNG_ARM_NEON_CHECK_SUPPORTED*/
#define PNG_BENIGN_ERRORS_SUPPORTED
#define PNG_BENIGN_READ_ERRORS_SUPPORTED
/*#undef PNG_BENIGN_WRITE_ERRORS_SUPPORTED*/
#define PNG_BUILD_GRAYSCALE_PALETTE_SUPPORTED
#define PNG_CHECK_FOR_INVALID_INDEX_SUPPORTED
#define PNG_COLORSPACE_SUPPORTED
#define PNG_CONSOLE_IO_SUPPORTED
#define PNG_CONVERT_tIME_SUPPORTED
#define PNG_EASY_ACCESS_SUPPORTED
/*#undef PNG_ERROR_NUMBERS_SUPPORTED*/
#define PNG_ERROR_TEXT_SUPPORTED
#define PNG_FIXED_POINT_SUPPORTED
#define PNG_FLOATING_ARITHMETIC_SUPPORTED
#define PNG_FLOATING_POINT_SUPPORTED
#define PNG_FORMAT_AFIRST_SUPPORTED
#define PNG_FORMAT_BGR_SUPPORTED
#define PNG_GAMMA_SUPPORTED
#define PNG_GET_PALETTE_MAX_SUPPORTED
#define PNG_HANDLE_AS_UNKNOWN_SUPPORTED
#define PNG_INCH_CONVERSIONS_SUPPORTED
#define PNG_INFO_IMAGE_SUPPORTED
#define PNG_IO_STATE_SUPPORTED
#define PNG_MNG_FEATURES_SUPPORTED
#define PNG_POINTER_INDEXING_SUPPORTED
#define PNG_PROGRESSIVE_READ_SUPPORTED
#define PNG_READ_16BIT_SUPPORTED
#define PNG_READ_ALPHA_MODE_SUPPORTED
#define PNG_READ_ANCILLARY_CHUNKS_SUPPORTED
#define PNG_READ_BACKGROUND_SUPPORTED
#define PNG_READ_BGR_SUPPORTED
#define PNG_READ_CHECK_FOR_INVALID_INDEX_SUPPORTED
#define PNG_READ_COMPOSITE_NODIV_SUPPORTED
#define PNG_READ_COMPRESSED_TEXT_SUPPORTED
#define PNG_READ_EXPAND_16_SUPPORTED
#define PNG_READ_EXPAND_SUPPORTED
#define PNG_READ_FILLER_SUPPORTED
#define PNG_READ_GAMMA_SUPPORTED
#define PNG_READ_GET_PALETTE_MAX_SUPPORTED
#define PNG_READ_GRAY_TO_RGB_SUPPORTED
#define PNG_READ_INTERLACING_SUPPORTED
#define PNG_READ_INT_FUNCTIONS_SUPPORTED
#define PNG_READ_INVERT_ALPHA_SUPPORTED
#define PNG_READ_INVERT_SUPPORTED
#define PNG_READ_OPT_PLTE_SUPPORTED
#define PNG_READ_PACKSWAP_SUPPORTED
#define PNG_READ_PACK_SUPPORTED
#define PNG_READ_QUANTIZE_SUPPORTED
#define PNG_READ_RGB_TO_GRAY_SUPPORTED
#define PNG_READ_SCALE_16_TO_8_SUPPORTED
#define PNG_READ_SHIFT_SUPPORTED
#define PNG_READ_STRIP_16_TO_8_SUPPORTED
#define PNG_READ_STRIP_ALPHA_SUPPORTED
#define PNG_READ_SUPPORTED
#define PNG_READ_SWAP_ALPHA_SUPPORTED
#define PNG_READ_SWAP_SUPPORTED
#define PNG_READ_TEXT_SUPPORTED
#define PNG_READ_TRANSFORMS_SUPPORTED
#define PNG_READ_UNKNOWN_CHUNKS_SUPPORTED
#define PNG_READ_USER_CHUNKS_SUPPORTED
#define PNG_READ_USER_TRANSFORM_SUPPORTED
#define PNG_READ_bKGD_SUPPORTED
#define PNG_READ_cHRM_SUPPORTED
#define PNG_READ_gAMA_SUPPORTED
#define PNG_READ_hIST_SUPPORTED
#define PNG_READ_iCCP_SUPPORTED
#define PNG_READ_iTXt_SUPPORTED
#define PNG_READ_oFFs_SUPPORTED
#define PNG_READ_pCAL_SUPPORTED
#define PNG_READ_pHYs_SUPPORTED
#define PNG_READ_sBIT_SUPPORTED
#define PNG_READ_sCAL_SUPPORTED
#define PNG_READ_sPLT_SUPPORTED
#define PNG_READ_sRGB_SUPPORTED
#define PNG_READ_tEXt_SUPPORTED
#define PNG_READ_tIME_SUPPORTED
#define PNG_READ_tRNS_SUPPORTED
#define PNG_READ_zTXt_SUPPORTED
#define PNG_SAVE_INT_32_SUPPORTED
#define PNG_SAVE_UNKNOWN_CHUNKS_SUPPORTED
#define PNG_SEQUENTIAL_READ_SUPPORTED
#define PNG_SETJMP_SUPPORTED
#define PNG_SET_CHUNK_CACHE_LIMIT_SUPPORTED
#define PNG_SET_CHUNK_MALLOC_LIMIT_SUPPORTED
#define PNG_SET_OPTION_SUPPORTED
#define PNG_SET_UNKNOWN_CHUNKS_SUPPORTED
#define PNG_SET_USER_LIMITS_SUPPORTED
#define PNG_SIMPLIFIED_READ_AFIRST_SUPPORTED
#define PNG_SIMPLIFIED_READ_BGR_SUPPORTED
#define PNG_SIMPLIFIED_READ_SUPPORTED
#define PNG_SIMPLIFIED_WRITE_AFIRST_SUPPORTED
#define PNG_SIMPLIFIED_WRITE_BGR_SUPPORTED
#define PNG_SIMPLIFIED_WRITE_SUPPORTED
#define PNG_STDIO_SUPPORTED
#define PNG_STORE_UNKNOWN_CHUNKS_SUPPORTED
#define PNG_TEXT_SUPPORTED
#define PNG_TIME_RFC1123_SUPPORTED
#define PNG_UNKNOWN_CHUNKS_SUPPORTED
#define PNG_USER_CHUNKS_SUPPORTED
#define PNG_USER_LIMITS_SUPPORTED
#define PNG_USER_MEM_SUPPORTED
#define PNG_USER_TRANSFORM_INFO_SUPPORTED
#define PNG_USER_TRANSFORM_PTR_SUPPORTED
#define PNG_WARNINGS_SUPPORTED
#define PNG_WRITE_16BIT_SUPPORTED
#define PNG_WRITE_ANCILLARY_CHUNKS_SUPPORTED
#define PNG_WRITE_BGR_SUPPORTED
#define PNG_WRITE_CHECK_FOR_INVALID_INDEX_SUPPORTED
#define PNG_WRITE_COMPRESSED_TEXT_SUPPORTED
#define PNG_WRITE_CUSTOMIZE_COMPRESSION_SUPPORTED
#define PNG_WRITE_CUSTOMIZE_ZTXT_COMPRESSION_SUPPORTED
#define PNG_WRITE_FILLER_SUPPORTED
#define PNG_WRITE_FILTER_SUPPORTED
#define PNG_WRITE_FLUSH_SUPPORTED
#define PNG_WRITE_GET_PALETTE_MAX_SUPPORTED
#define PNG_WRITE_INTERLACING_SUPPORTED
#define PNG_WRITE_INT_FUNCTIONS_SUPPORTED
#define PNG_WRITE_INVERT_ALPHA_SUPPORTED
#define PNG_WRITE_INVERT_SUPPORTED
#define PNG_WRITE_OPTIMIZE_CMF_SUPPORTED
#define PNG_WRITE_PACKSWAP_SUPPORTED
#define PNG_WRITE_PACK_SUPPORTED
#define PNG_WRITE_SHIFT_SUPPORTED
#define PNG_WRITE_SUPPORTED
#define PNG_WRITE_SWAP_ALPHA_SUPPORTED
#define PNG_WRITE_SWAP_SUPPORTED
#define PNG_WRITE_TEXT_SUPPORTED
#define PNG_WRITE_TRANSFORMS_SUPPORTED
#define PNG_WRITE_UNKNOWN_CHUNKS_SUPPORTED
#define PNG_WRITE_USER_TRANSFORM_SUPPORTED
#define PNG_WRITE_WEIGHTED_FILTER_SUPPORTED
#define PNG_WRITE_bKGD_SUPPORTED
#define PNG_WRITE_cHRM_SUPPORTED
#define PNG_WRITE_gAMA_SUPPORTED
#define PNG_WRITE_hIST_SUPPORTED
#define PNG_WRITE_iCCP_SUPPORTED
#define PNG_WRITE_iTXt_SUPPORTED
#define PNG_WRITE_oFFs_SUPPORTED
#define PNG_WRITE_pCAL_SUPPORTED
#define PNG_WRITE_pHYs_SUPPORTED
#define PNG_WRITE_sBIT_SUPPORTED
#define PNG_WRITE_sCAL_SUPPORTED
#define PNG_WRITE_sPLT_SUPPORTED
#define PNG_WRITE_sRGB_SUPPORTED
#define PNG_WRITE_tEXt_SUPPORTED
#define PNG_WRITE_tIME_SUPPORTED
#define PNG_WRITE_tRNS_SUPPORTED
#define PNG_WRITE_zTXt_SUPPORTED
#define PNG_bKGD_SUPPORTED
#define PNG_cHRM_SUPPORTED
#define PNG_gAMA_SUPPORTED
#define PNG_hIST_SUPPORTED
#define PNG_iCCP_SUPPORTED
#define PNG_iTXt_SUPPORTED
#define PNG_oFFs_SUPPORTED
#define PNG_pCAL_SUPPORTED
#define PNG_pHYs_SUPPORTED
#define PNG_sBIT_SUPPORTED
#define PNG_sCAL_SUPPORTED
#define PNG_sPLT_SUPPORTED
#define PNG_sRGB_SUPPORTED
#define PNG_tEXt_SUPPORTED
#define PNG_tIME_SUPPORTED
#define PNG_tRNS_SUPPORTED
#define PNG_zTXt_SUPPORTED
/* end of options */
/* settings */
#define PNG_API_RULE 0
#define PNG_COST_SHIFT 3
#define PNG_DEFAULT_READ_MACROS 1
#define PNG_GAMMA_THRESHOLD_FIXED 5000
#define PNG_IDAT_READ_SIZE PNG_ZBUF_SIZE
#define PNG_INFLATE_BUF_SIZE 1024
#define PNG_MAX_GAMMA_8 11
#define PNG_QUANTIZE_BLUE_BITS 5
#define PNG_QUANTIZE_GREEN_BITS 5
#define PNG_QUANTIZE_RED_BITS 5
#define PNG_TEXT_Z_DEFAULT_COMPRESSION (-1)
#define PNG_TEXT_Z_DEFAULT_STRATEGY 0
#define PNG_USER_CHUNK_CACHE_MAX 1000
#define PNG_USER_CHUNK_MALLOC_MAX 8000000
#define PNG_USER_HEIGHT_MAX 1000000
#define PNG_USER_WIDTH_MAX 1000000
#define PNG_WEIGHT_SHIFT 8
#define PNG_ZBUF_SIZE 8192
#define PNG_ZLIB_VERNUM 0 /* unknown */
#define PNG_Z_DEFAULT_COMPRESSION (-1)
#define PNG_Z_DEFAULT_NOFILTER_STRATEGY 0
#define PNG_Z_DEFAULT_STRATEGY 1
#define PNG_sCAL_PRECISION 5
#define PNG_sRGB_PROFILE_CHECKS 2
/* end of settings */
#endif /* PNGLCONF_H */
'''