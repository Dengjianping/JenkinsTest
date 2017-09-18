#ifndef _SIMPLEMATH_H_
#define _SIMPLEMATH_H_

#ifdef LIBDLL
	#define LIBDLL extern "C" _declspec(dllimport)
#else
	#define LIBDLL extern "C" _declspec(dllexport)
#endif


#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

LIBDLL int add(int *x, int *y);
LIBDLL int sub(int x, int y);

#endif // DEBUG