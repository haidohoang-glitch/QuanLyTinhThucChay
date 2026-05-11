# Stored Procedure: `SP_InsertOrUpdate_HopDongLog_FROM_TOOLCONTRACT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-14 11:39:30.743000
- **Ngày sửa cuối**: 2021-10-27 17:24:39.710000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[SP_InsertOrUpdate_HopDongLog_FROM_TOOLCONTRACT] 	
AS
BEGIN
	DECLARE @MaxLogTime DATETIME
	DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''

	SET @MaxLogTime =
	ISNULL((Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[HopDongLog] Where 1=1  and DeletedStatus <> 1 AND GhiChu = 'SYN_TOOL_CONTRACT'),'2010-01-01')

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')
	
SET @SQL =
	'INSERT INTO dbo.HopDongLog
	        ( HopDongID ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          SO ,
	          Thang ,
	          Nam ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          GiaTriHopDong ,
	          SoHopDong ,
	          ThucHienDenNgayThucChay ,
	          ThanhTienThucChay ,
	          ThucHienDenNgayHoaDon ,
	          ThanhTienHoaDon ,
	          ThucHienDenNgayCongNo ,
	          ThanhTienCongNo ,
	          NgayChuyenHopDongChoKeToan ,
	          GhiChu ,
	          NgayNhanHopDongBanCung ,
	          DmKhachHangREF ,
	          TenKhachHang ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          NgayDanhSoHopDong ,
	          NganhHang ,
	          DmNhomREF ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          CongNo ,
	          GhiChuHopDong ,
	          NgayNhanBanFax ,
	          LyDoHuyHopDong ,
	          DangSuDung ,
	          IsGiayPhep ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhom ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          ChuyenTrang ,
	          IsUuDai ,
	          ThoiGianLog ,
	          NguoiLog ,
	          LoaiLog ,
	          CreatedBy ,
	          CreatedAt ,
	          LastModifiedBy ,
	          LastModifiedAt ,
	          DeletedStatus ,
	          PrintStatus ,
	          RecordStatus
	        ) '
	SET @SQL +=
	'SELECT d.Contract_id HopDongID
	, d.Contract_prefix_code_id DmMaHopDongREF
	, '''' TenMaHopDong
	, d.Contract_number_month So
	, d.Contract_month thang
	, d.Contract_year nam
	, d.Signed_date NgayKyHopDong
	, d.root_brand_name NhanHopDong
	, d.TOTAL_VALUE GiaTriHopDong
	, d.contract_number SoHopDong
	, '''' ThucHIenDenNgayThucChay
	, 0 ThanhTienThucChay
	, '''' ThucHienDenNgayHoaDon
	, 0 ThanhTienHoaDon
	, '''' ThucHienDenNgayCongNo
	, 0 ThanhTienCongNo
	, d.Date_transport_accounting NgayChuyenHopDongChoKeToan
	, '+ @daunhay + 'SYN_TOOL_CONTRACT' + @daunhay + ' GhiChu 
	, '''' NgayNhanBanCung
	, d.customer_id DmKhachHangREF
	, '''' TenKhachHang
	, d.staff_id SysNhanVienREF
	, '''' TenDangNhap
	, '''' TenNhanVien
	, d.Indexed_date NgayDanhSoHOpDong
	, '''' NganhHang
	, d.Team_id DmNhomREF
	, d.status TrangThaiHopDong
	, d.is_couple_signed IsBanCung
	, 0 CongNo
	, d.Note GhiChuHopDong
	, d.DATE_ACCEPT_FAX NgayNhanBanFax
	, '''' LyHuyHopDong
	, d.Voucher_contract_use DangSuDung
	, 0 IsGiayPhep
	, d.department_id DmPhongBanREF
	, '''' TenPhongBan
	, d.work_group_id  DmBoPhanREF
	, '''' TenBoPhan
	, d.team_id DmNhomLamViecREF
	, '''' TenNhom
	, d. staff_location_id DmDiaDiemLamViecREF
	, '''' TenDiaDiemLamViec
	, 0 ChuyenTrang
	, d.Is_endow IsUuDai
	, d.last_modified_at
	, d.Last_modified_by
	, d.LOG_STATUS LoaiLog
	, d.created_by
	, d.created_at
	, d.Last_modified_by
	, d.last_modified_at
	, d.Deleted_status
	, 0 PrintStatus
	, 0 RecordStatus
	FROM ' + @server_id + '.' + @database + '.dbo.Contract_log d
	WHERE  d.LAST_MODIFIED_AT > ' + @daunhay + convert(nvarchar(23),@MaxLogTime,121)+ @daunhay+' '
	

	--PRINT @SQL
	EXEC(@SQL)
END

```
