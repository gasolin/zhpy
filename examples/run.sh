echo "zhpy hello example"

cd hello
zhpy -p hello.py
cd ..

echo "zhpy in/out example"
cd inout
zhpy -p inout.py
cd ..

echo "zhpy loop example"
cd loop
zhpy -p tabl.py
cd ..

echo "zhpy game example, pygame module required. Use 'Ctrl+c' to escape"

cd game
zhpy -p game.py
cd ..

echo "finish"