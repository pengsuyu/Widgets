import biplist
import plistlib

def convert_binary_plist_to_xml(binary_plist_path, xml_plist_path):
    try:
        # 读取二进制 plist 文件
        plist_data = biplist.readPlist(binary_plist_path)
        
        # 将数据转换为 XML 格式
        with open(xml_plist_path, 'wb') as xml_file:
            plistlib.dump(plist_data, xml_file, fmt=plistlib.FMT_XML)
        
        print(f"Conversion successful. XML plist saved to: {xml_plist_path}")
    except biplist.InvalidPlistException as e:
        print(f"Invalid plist file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 输入和输出文件路径
binary_plist_path = "Info.plist"
xml_plist_path = "Info.xml"

# 调用转换函数
convert_binary_plist_to_xml(binary_plist_path, xml_plist_path)