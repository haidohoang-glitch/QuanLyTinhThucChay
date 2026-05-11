# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_NgayThucHien_SanPham_ByHDCT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-30 15:55:17.763000
- **Ngày sửa cuối**: 2018-08-30 15:55:17.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HDCT` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_NgayThucHien_SanPham_ByHDCT]
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT,
	@HDCT INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    declare 
	@HopDongID INT,
	@HopDongChiTietID INT,
	@ThucChayHopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@DmKhachHangREF_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsNhanHangREF_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50),
	@MaSoHopDong_new INT , @Note NVARCHAR(50), @IsThayDoi INT,@GiaTriThucChay FLOAT,@GiaTriThucChayAd FLOAT, @IsExistData INT ,@IsExistData1 INT  ;
	DECLARE @out NVARCHAR(2000);

	--- Update nhan hang bởi thực chạy hd chi tiết
	DECLARE @NhanHangMoi NVARCHAR(500),@HDID INT, @PhanBoID INT 
	DECLARE cursor_hdct CURSOR FOR  
		SELECT tc.HopDongREF, tc.HopDongChiTietREF, Lg.ThucChayHopDongChiTietID, tc.DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet tc 
		INNER JOIN
		(
			SELECT * FROM
			(
				SELECT ROW_NUMBER() OVER (PARTITION BY ThucChayHopDongChiTietID ORDER By ThucChayHopDongChiTietID ASC ,ThoiGianLog ASC) as stt,
				ThucChayHopDongChiTietID, HopDongREF, HopDongChiTietREF, DmNhanHangREF, NhanHang, ThoiGianLog
				FROM dbo.ThucChayHopDongChiTietLog
				WHERE CONVERT(DATE,ThoiGianLog) = @NgayThucHien
			)A
			WHERE a.stt =1
		)Lg ON tc.ThucChayHopDongChiTietID = Lg.ThucChayHopDongChiTietID AND Lg.DmNhanHangREF <> tc.DmNhanHangREF
		INNER JOIN dbo.HopDong hd ON hd.HopDongID = tc.HopDongREF
		WHERE tc.DmSanPhamREF IN (140,228,240,241,242,243,251,252,253,300,339,342,370,385,531,535,540,541,549,560,563,
									586,598,613,629,630,631,632,633,634,635,636, 736
														, 734
														, 771
														, 772
														, 775 --Campaign Audit
														, 729
														, 792, 805
														, 806,817)
			AND tc.DmHinhThucQuangCaoREF NOT IN (42)
			AND YEAR(hd.NgayDanhSoHopDong) >= YEAR(GETDATE()) - 2 --2017-03-15 HAIDH COMMENT KHONG TINH GIA TRI THAY DOI SAU 2 NAM SO VOI NAM HIEN TAI
			AND tc.DmSanPhamREF = @DmSanPhamREF
			AND tc.HopDongChiTietREF = @HDCT
		OPEN cursor_hdct   	
	FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID, @ThucChayHopDongChiTietID, @NhanHangMoi   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		
		EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang] @NgayThucHien ,@HDID ,@PhanBoID , @ThucChayHopDongChiTietID
		
	FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID, @ThucChayHopDongChiTietID, @NhanHangMoi    
	END   

	CLOSE cursor_hdct   
	DEALLOCATE cursor_hdct
	
END



```
