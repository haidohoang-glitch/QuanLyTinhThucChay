# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:24.993000
- **Ngày sửa cuối**: 2024-10-07 15:51:32.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHIen` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD] 
	@NgayThucHIen DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT,@SoHopDong NVARCHAR(50),@HopDongChiTietID INT
	DECLARE @SoLuongDotChayHD INT,@ThanhTienHDCT FLOAT, @count_hdct INT
	, @NgayDanhSo_GioiHan DATETIME

	set @count_hdct = 0
	SET @NgayDanhSo_GioiHan = DATEADD(yyyy,-3,GETDATE())

	DECLARE Record_Cursor CURSOR FOR 
   
   --1. Xác định phân bổ có thay đổi thông tin đánh số
	SELECT hd.HopDongID, hd.SoHopDong, hdcttd.HopDongChiTietREF, hdcttd.SoLuong, hdcttd.ThanhTien
	  FROM HopDong hd
	INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
	INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
	AND Convert(date,hdtd.NgayThayDoi) = @NgayThucHien
	AND hdcttd.DmSanPhamREF IN (140,228,241,564,549,5082)
	AND hdcttd.DmLoaiREF <> 13 
	AND  Upper((RTrim(LTrim(hdcttd.DonViTinh)))) IN (N'NGÀY' , N'TUẦN' , N'THÁNG' , N'NĂM' )
	AND exists (select top 1 dc.HopDongChiTietREF from dbo.DotChayHopDongchitiet dc WHERE dc.HopDongChiTietREF = hdcttd.HopDongChiTietREF)--check co dot chay 02/12/2022
	WHERE hd.TrangThaiHopDong <> 3
	AND hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan

	ORDER BY hd.SoHopDong	
	
	OPEN Record_Cursor

	--2. Đối trừ KM
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @count_hdct = 
			(
				SELECT count(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID	
				AND hdct.DeletedStatus = 0
			)
			-- TH phân bổ có thay đổi về đơn giá, số lượng, chiết khấu
			IF(@count_hdct > 0) 
				EXEC ThucChay_CheckHopDongCoThayDoi_CPDDotChay @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
			-- TH phân bổ bị xóa
			ELSE
				EXEC ThucChay_CheckHopDongXoaPhanBo_CPD @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
			set @count_hdct = 0				
		FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
		END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD] '2013-09-03'

```
