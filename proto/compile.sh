# bin/bash
for FILE in $(find proto -name "*.proto"); # 找到 proto 目录下以 proto 后缀结尾的文件，然后逐个编译
# for FILE in $(find proto -name "*.proto"); do PKG=$(basename $(dirname $FILE)); echo "look for package $PKG in $FILE"; grep -q "^package $PKG;$" $FILE; done'
do
#  PKG=$(basename $(dirname $FILE));
#  echo "look for package $PKG in $FILE";
#  grep -q "^package $PKG;$" $FILE;
  python -m grpc_tools.protoc -I . --python_out=.  $FILE
  echo "python -m grpc_tools.protoc -I . --python_out=.  $FILE";
done