# Stored Procedure: `InsertOrUpdate_HopDongTongHop_ByJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-03 08:45:04.550000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.677000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[InsertOrUpdate_HopDongTongHop_ByJobs]

AS
BEGIN


DECLARE 
           @HopDongID int
           ,@DmMaHopDongREF int
           ,@TenMaHopDong nvarchar(50)
           ,@So nvarchar(50)
           ,@Thang int
           ,@Nam int
           ,@NgayKyHopDong datetime
           ,@NhanHopDong nvarchar(50)
           ,@GiaTriHopDong float
           ,@SoHopDong nvarchar(50)
           ,@NgayChuyenHopDongChoKeToan datetime
           ,@GhiChu nvarchar(300)
           ,@NgayNhanHopDongBanCung datetime
           ,@DmKhachHangREF int
           ,@TenKhachHang nvarchar(255)
           ,@SysNhanVienREF int
           ,@TenDangNhap nvarchar(25)
           ,@TenNhanVien nvarchar(100)
           ,@NgayDanhSoHopDong datetime
           ,@NganhHang nvarchar(50)
           ,@DmNhomREF int
           ,@TrangThaiHopDong int
           ,@IsBanCung int
           ,@CongNo float
           ,@GhiChuHopDong nvarchar(4000)
           ,@NgayNhanBanFax datetime
           ,@LyDoHuyHopDong nvarchar(4000)
           ,@DangSuDung int
           ,@IsGiayPhep int
           ,@DmPhongBanREF int
           ,@TenPhongBan nvarchar(50)
           ,@DmBoPhanREF int
           ,@TenBoPhan nvarchar(50)
           ,@DmNhomLamViecREF int
           ,@TenNhom nvarchar(50)
           ,@DmDiaDiemLamViecREF int
           ,@TenDiaDiemLamViec nvarchar(50)
           ,@ChuyenTrang int
           ,@CreatedBy nvarchar(50)
           ,@CreatedAt datetime
           ,@LastModifiedBy nvarchar(50)
           ,@LastModifiedAt datetime
           ,@DeletedStatus int
           ,@PrintStatus int
           ,@RecordStatus INT
           --,@TongTienHopDong FLOAT
           ,@TongTienThucChay FLOAT
           ,@TongTienChuaChay FLOAT
           ,@TongTienXuatHoaDon FLOAT
           ,@TongTienDaThanhToan FLOAT
           ,@TrangThaiThucChayHopDong INT 
           ,@ThucChayDenNgay DATETIME
           ,@HoaDonDenNgay DATETIME
           ,@TienDaThanhToanDenNgay DATETIME
           ,@TongTienKyHopDong FLOAT
           ,@TongTienHaiDauHopDong FLOAT
           
           
--A.NgayKyHopDong changby tuanln 18.11.2014
--A.LastModifiedAt >= (SELECT MAX(LastModifiedAt) FROM dbo.HopDongTongHop)
DECLARE @COUNT INT
SET @COUNT = 0;
DECLARE Record_Cursor CURSOR FOR 
	SELECT * FROM dbo.HopDong A
	WHERE A.HopDongID IN (SELECT B.HopDongID FROM HopDong B WHERE B.HopDongID NOT IN (SELECT HopDongID FROM HopDongTongHop))
	ORDER BY A.LastModifiedAt

OPEN Record_Cursor

FETCH NEXT FROM Record_Cursor into 
 	   @HopDongID
      ,@DmMaHopDongREF
      ,@TenMaHopDong
      ,@So
      ,@Thang
      ,@Nam
      ,@NgayKyHopDong
      ,@NhanHopDong
      ,@GiaTriHopDong
      ,@SoHopDong
      ,@NgayChuyenHopDongChoKeToan
      ,@GhiChu
      ,@NgayNhanHopDongBanCung
      ,@DmKhachHangREF
      ,@TenKhachHang
      ,@SysNhanVienREF
      ,@TenDangNhap
      ,@TenNhanVien
      ,@NgayDanhSoHopDong
      ,@NganhHang
      ,@DmNhomREF
      ,@TrangThaiHopDong
      ,@IsBanCung
      ,@CongNo
      ,@GhiChuHopDong
      ,@NgayNhanBanFax
      ,@LyDoHuyHopDong
      ,@DangSuDung
      ,@IsGiayPhep
      ,@DmPhongBanREF
      ,@TenPhongBan
      ,@DmBoPhanREF
      ,@TenBoPhan
      ,@DmNhomLamViecREF
      ,@TenNhom
      ,@DmDiaDiemLamViecREF
      ,@TenDiaDiemLamViec
      ,@ChuyenTrang
      ,@CreatedBy
      ,@CreatedAt
      ,@LastModifiedBy
      ,@LastModifiedAt
      ,@DeletedStatus
      ,@PrintStatus
      ,@RecordStatus

WHILE @@FETCH_STATUS = 0
	BEGIN

	SET @COUNT = @COUNT + 1;
	PRINT @COUNT;
      --SET @TongTienHopDong = @GiaTriHopDong
							
							
	  --SET @TongTienHopDong = @TongTienHopDong + @TongTienHopDong*0.1
	  
	  --SET @TongTienHopDong = ISNULL(@TongTienHopDong,0)
	  
      SET @TongTienThucChay = (SELECT SUM(ThanhTienDaChay) FROM dbo.ThucChayTheoDoiHopDongChiTiet
							WHERE HopDongFK = @HopDongID)
							
      SET @TongTienThucChay = 	@TongTienThucChay+ @TongTienThucChay*0.1
      
      SET @TongTienThucChay = ISNULL(@TongTienThucChay,0)
      		
      SET @ThucChayDenNgay = (SELECT MAX(ThucChayDenNgay) FROM dbo.ThucChayTheoDoiHopDongChiTiet
							WHERE HopDongFK = @HopDongID)
							 
             		
      SET @TongTienChuaChay = (SELECT SUM(ThanhTienChuaChay) FROM dbo.ThucChayTheoDoiHopDongChiTiet
							WHERE HopDongFK = @HopDongID)
							
	  SET @TongTienChuaChay = @TongTienChuaChay + @TongTienChuaChay*0.1
	  
	  SET @TongTienChuaChay = ISNULL(@TongTienChuaChay,0)
	  
      SET @TongTienXuatHoaDon = (SELECT SUM(GiaTri) FROM dbo.CongNo
							WHERE HopDongREF = @HopDongID)
							
	  SET @TongTienXuatHoaDon = ISNULL(@TongTienXuatHoaDon,0)
	   
	  SET @HoaDonDenNgay = (SELECT MAX(NgayXuat) FROM dbo.CongNo
							WHERE HopDongREF = @HopDongID)
							
      SET @TongTienDaThanhToan = (SELECT SUM(GiaTriThanhToan) FROM dbo.CongNo
							WHERE HopDongREF = @HopDongID)

	  SET @TongTienDaThanhToan = ISNULL(@TongTienDaThanhToan,0)
	 
	  SET @TienDaThanhToanDenNgay = (SELECT MAX(NgayThanhToan) FROM dbo.CongNo
							WHERE HopDongREF = @HopDongID)
	  
	  SET @TrangThaiThucChayHopDong = dbo.GetTrangThaiThucChayHopDong(@HopDongID)
	
	  SET @TongTienKyHopDong =  (SELECT SUM(ThanhTien) FROM dbo.ThucChayTheoDoiHopDongChiTiet A
									INNER JOIN dbo.HopDong B ON A.HopDongFK = B.HopDongID
							WHERE A.HopDongFK = @HopDongID AND B.IsBanCung =0)
	  
	  SET @TongTienKyHopDong =  @TongTienKyHopDong + @TongTienKyHopDong*0.1
	  	
	  SET @TongTienKyHopDong = ISNULL(@TongTienKyHopDong,0)
	  
	  
	  SET @TongTienHaiDauHopDong =  (SELECT SUM(ThanhTien) FROM dbo.ThucChayTheoDoiHopDongChiTiet A
									INNER JOIN dbo.HopDong B ON A.HopDongFK = B.HopDongID
							WHERE A.HopDongFK = @HopDongID AND B.IsBanCung =1)	
	  
	  SET @TongTienHaiDauHopDong = @TongTienHaiDauHopDong + @TongTienHaiDauHopDong*0.1
	  
	  SET @TongTienHaiDauHopDong = ISNULL(@TongTienHaiDauHopDong,0)
	  
	  
IF(EXISTS(SELECT * FROM HopDongTongHop WHERE HopDongID = @HopDongID))
BEGIN
  
UPDATE [dbo].[HopDongTongHop]
   SET 
      [DmMaHopDongREF] = @DmMaHopDongREF
      ,[TenMaHopDong] = @TenMaHopDong
      ,[So] = @So
      ,[Thang] = @Thang
      ,[Nam] = @Nam
      ,[NgayKyHopDong] = @NgayKyHopDong
      ,[NhanHopDong] = @NhanHopDong
      ,[GiaTriHopDong] = @GiaTriHopDong
      ,[SoHopDong] = @SoHopDong
      ,[NgayChuyenHopDongChoKeToan] = @NgayChuyenHopDongChoKeToan
      ,[GhiChu] = @GhiChu
      ,[NgayNhanHopDongBanCung] = @NgayNhanHopDongBanCung
      ,[DmKhachHangREF] = @DmKhachHangREF
      ,[TenKhachHang] = @TenKhachHang
      ,[SysNhanVienREF] = @SysNhanVienREF
      ,[TenDangNhap] = @TenDangNhap
      ,[TenNhanVien] = @TenNhanVien
      ,[NgayDanhSoHopDong] = @NgayDanhSoHopDong
      ,[NganhHang] = @NganhHang
      ,[DmNhomREF] = @DmNhomREF
      ,[TrangThaiHopDong] = @TrangThaiHopDong
      ,[IsBanCung] = @IsBanCung
      ,[CongNo] = @CongNo
      ,[GhiChuHopDong] = @GhiChuHopDong
      ,[NgayNhanBanFax] = @NgayNhanBanFax
      ,[LyDoHuyHopDong] = @LyDoHuyHopDong
      ,[DangSuDung] = @DangSuDung
      ,[IsGiayPhep] = @IsGiayPhep
      ,[DmPhongBanREF] = @DmPhongBanREF
      ,[TenPhongBan] = @TenPhongBan
      ,[DmBoPhanREF] = @DmBoPhanREF
      ,[TenBoPhan] = @TenBoPhan
      ,[DmNhomLamViecREF] = @DmNhomLamViecREF
      ,[TenNhom] = @TenNhom
      ,[DmDiaDiemLamViecREF] = @DmDiaDiemLamViecREF
      ,[TenDiaDiemLamViec] = @TenDiaDiemLamViec
      ,[ChuyenTrang] = @ChuyenTrang
      ,[TrangThaiThucChayHopDong] = @TrangThaiThucChayHopDong
      --,[TongTienHopDong] = @TongTienHopDong
      ,[TongTienKyHopDong] = @TongTienKyHopDong
      ,[TongTienHaiDauHopDong] = @TongTienHaiDauHopDong
      ,[ThucChayDenNgay] = @ThucChayDenNgay
      ,[TongTienThucChay] = @TongTienThucChay
      ,[TongTienChuaChay] = @TongTienChuaChay
      ,[HoaDonDenNgay] = @HoaDonDenNgay
      ,[TongTienXuatHoaDon] = @TongTienXuatHoaDon
      ,[TienDaThanhToanDenNgay] = @TienDaThanhToanDenNgay
      ,[TongTienDaThanhToan] = @TongTienDaThanhToan
      --,[TongTienCongNo] = (@TongTienHopDong - @TongTienDaThanhToan)
      ,[CreatedBy] = @CreatedBy
      ,[CreatedAt] = @CreatedAt
      ,[LastModifiedBy] = @LastModifiedBy
      ,[LastModifiedAt] = @LastModifiedAt
      ,[DeletedStatus] = @DeletedStatus
      ,[PrintStatus] = @PrintStatus
      ,[RecordStatus] = @RecordStatus
 WHERE [HopDongID] = @HopDongID	

End
ELSE
BEGIN
INSERT INTO dbo.HopDongTongHop
	SELECT 
			@HopDongID
           ,@DmMaHopDongREF
           ,@TenMaHopDong
           ,@So
           ,@Thang
           ,@Nam
           ,@NgayKyHopDong
           ,@NhanHopDong
           ,@GiaTriHopDong
           ,@SoHopDong
           ,@NgayChuyenHopDongChoKeToan
           ,@GhiChu
           ,@NgayNhanHopDongBanCung
           ,@DmKhachHangREF
           ,@TenKhachHang
           ,@SysNhanVienREF
           ,@TenDangNhap
           ,@TenNhanVien
           ,@NgayDanhSoHopDong
           ,@NganhHang
           ,@DmNhomREF
           ,@TrangThaiHopDong
           ,@IsBanCung
           ,@CongNo
           ,@GhiChuHopDong
           ,@NgayNhanBanFax
           ,@LyDoHuyHopDong
           ,@DangSuDung
           ,@IsGiayPhep
           ,@DmPhongBanREF
           ,@TenPhongBan
           ,@DmBoPhanREF
           ,@TenBoPhan
           ,@DmNhomLamViecREF
           ,@TenNhom
           ,@DmDiaDiemLamViecREF
           ,@TenDiaDiemLamViec
           ,@ChuyenTrang
           ,@TrangThaiThucChayHopDong
		   --,@TongTienHopDong
           ,@TongTienKyHopDong
           ,@TongTienHaiDauHopDong		  
		  ,@ThucChayDenNgay
		  ,@TongTienThucChay
		  ,@TongTienChuaChay
		  ,@HoaDonDenNgay
		  ,@TongTienXuatHoaDon
		  ,@TienDaThanhToanDenNgay
		  ,@TongTienDaThanhToan
		  --,(@TongTienHopDong - @TongTienDaThanhToan)			
           ,@CreatedBy
           ,@CreatedAt
           ,@LastModifiedBy
           ,@LastModifiedAt
           ,@DeletedStatus
           ,@PrintStatus
           ,@RecordStatus

END
  
	FETCH NEXT FROM Record_Cursor into 
	   @HopDongID
      ,@DmMaHopDongREF
      ,@TenMaHopDong
      ,@So
      ,@Thang
      ,@Nam
      ,@NgayKyHopDong
      ,@NhanHopDong
      ,@GiaTriHopDong
      ,@SoHopDong
      ,@NgayChuyenHopDongChoKeToan
      ,@GhiChu
      ,@NgayNhanHopDongBanCung
      ,@DmKhachHangREF
      ,@TenKhachHang
      ,@SysNhanVienREF
      ,@TenDangNhap
      ,@TenNhanVien
      ,@NgayDanhSoHopDong
      ,@NganhHang
      ,@DmNhomREF
      ,@TrangThaiHopDong
      ,@IsBanCung
      ,@CongNo
      ,@GhiChuHopDong
      ,@NgayNhanBanFax
      ,@LyDoHuyHopDong
      ,@DangSuDung
      ,@IsGiayPhep
      ,@DmPhongBanREF
      ,@TenPhongBan
      ,@DmBoPhanREF
      ,@TenBoPhan
      ,@DmNhomLamViecREF
      ,@TenNhom
      ,@DmDiaDiemLamViecREF
      ,@TenDiaDiemLamViec
      ,@ChuyenTrang
      ,@CreatedBy
      ,@CreatedAt
      ,@LastModifiedBy
      ,@LastModifiedAt
      ,@DeletedStatus
      ,@PrintStatus
      ,@RecordStatus
      	
	END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

	

	
END

```
