#include <chrono>
#include <iostream>
#include "solver.h"

int main(int argc, char** argv) {
  bool benchmark = false;
  for (int i = 1; i < argc; ++i) {
    char param = argv[i][1];
    if (param == 'b') {
      benchmark = true;
    }
  }
  auto solver = ej2::Solver();
  int iterations = benchmark ? 100 : 1;
  int solution;
  auto t_initial = std::chrono::high_resolution_clock::now();
  for (int iter = 0; iter < iterations; ++iter) {
    solution = solver.Solve();
  }
  auto t_final = std::chrono::high_resolution_clock::now();
  auto ellapsed_time =
      std::chrono::duration_cast<std::chrono::microseconds>(t_final - t_initial)
          .count();
  std::cout << (benchmark ? ellapsed_time : solution) << std::endl;
  return 0;
}
