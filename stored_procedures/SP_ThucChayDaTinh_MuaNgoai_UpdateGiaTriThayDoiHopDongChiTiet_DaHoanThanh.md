# Stored Procedure: `ThucChayDaTinh_MuaNgoai_UpdateGiaTriThayDoiHopDongChiTiet_DaHoanThanh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-12 16:46:57.340000
- **Ngày sửa cuối**: 2017-01-07 09:19:15.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.[ThucChayDaTinh_MuaNgoai_UpdateGiaTriThayDoiHopDongChiTiet_DaHoanThanh] '2016-12-31'
*/

CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_UpdateGiaTriThayDoiHopDongChiTiet_DaHoanThanh]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	DECLARE @ThanhTien BIGINT, @SoLuong BIGINT, @HopDongChiTietID INT, @DonViTinh NVARCHAR(100),@DonGia BIGINT,
	@thanhTienThucChayTCDT BIGINT=0, @thanhTienKhuyenMaiTCDT BIGINT =0,
	@soLuongThucChay BIGINT =0,@thucChayTruocChietKhau BIGINT=0,
	@thanhTienThucChay BIGINT=0,@soLuongThayDoi BIGINT=0,
	@giaTriThayDoi BIGINT =0,@soLuongKhuyenMai BIGINT=0,
	@thanhTienKhuyenMai BIGINT =0,@soLuongKMThayDoi BIGINT=0,
	@giaTriKMThayDoi BIGINT =0,@donViTinhThucChay NVARCHAR(100) ='',
	@ghiChu NVARCHAR(MAX)='', @ChietKhau INT = 0
    
	DECLARE pb_cursor CURSOR FOR
	
	--DANH SACH HOPDONGCHITIET DA HOAN THANH THUC CHAY MUA NGOAI
	SELECT hdct.HopDongChiTietID, hdct.ThanhTien, hdct.SoLuong, hdct.DonGia
	, @NgayThucHien 
	FROM dbo.HopDong hd
	INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	where hd.TrangThaiHopDong <> 3
	AND hd.DeletedStatus = 0
	AND hdct.DeletedStatus = 0
	AND (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
--	AND hd.HopDongID IN (
--44552
--)
	AND hdct.HopDongChiTietID IN (
	91513,
108282,
106869,
107796,
106861,
101870,
104999,
106872,
107795,
105929,
108281
)
		
	OPEN pb_cursor

	FETCH NEXT FROM pb_cursor INTO @HopDongChiTietID, @ThanhTien, @SoLuong, @DonGia, @ngayThucHien
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--ISNULL(dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(A.SoluongThucChay,A.DonViTinhThucChayMuaNgoai),0)
		-- dbo.FormatDonViTinh(A.DonViTinhThucChayMuaNgoai),
		IF(EXISTS(SELECT TOP 1 * FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietID)
		)
		BEGIN
			--XAC DINH GIA TRI THUC CHAY
			SELECT @thanhTienThucChayTCDT = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
			,@thanhTienKhuyenMaiTCDT = SUM(ThanhTienKM + GiaTriKMThayDoi)
			,@donViTinhThucChay = DonViTinh
			,@ChietKhau = ChietKhau
			FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF= @HopDongChiTietID
			GROUP BY DonViTinh, ChietKhau

			IF(@ChietKhau  <> 100)
			BEGIN
				SET @soLuongThucChay = 0
				SET @thucChayTruocChietKhau  =0
				SET @thanhTienThucChay =0
				SET @soLuongThayDoi =0
				SET @giaTriThayDoi = @ThanhTien- @thanhTienThucChayTCDT
				SET @soLuongKhuyenMai = 0
				SET @thanhTienKhuyenMai =0
				SET @soLuongKMThayDoi =0
				SET @giaTriKMThayDoi =0
				SET @DonViTinh = @donViTinhThucChay
				SET @ghiChu ='MUANGOAI_HOANTHANH_2016'
			END
				
			ELSE
				BEGIN
					SET @soLuongThucChay = 0
					SET @thucChayTruocChietKhau  =0
					SET @thanhTienThucChay =0
					SET @soLuongThayDoi =0
					SET @giaTriThayDoi = 0
					SET @soLuongKhuyenMai = 0
					SET @thanhTienKhuyenMai =0
					SET @soLuongKMThayDoi =0
					SET @giaTriKMThayDoi = @DonGia*@SoLuong - @thanhTienKhuyenMaiTCDT
					SET @DonViTinh = @donViTinhThucChay
					SET @ghiChu ='MUANGOAI_HOANTHANH_2016'
					
				END
		END
		ELSE
		BEGIN
			IF(@ChietKhau  <> 100)
			BEGIN
				SET @soLuongThucChay = @SoLuong
				SET @thucChayTruocChietKhau  =@DonGia*@SoLuong
				SET @thanhTienThucChay =@ThanhTien
				SET @soLuongThayDoi =0
				SET @giaTriThayDoi = 0
				SET @soLuongKhuyenMai = 0
				SET @thanhTienKhuyenMai =0
				SET @soLuongKMThayDoi =0
				SET @giaTriKMThayDoi =0
				SET @DonViTinh = @donViTinhThucChay
				SET @ghiChu ='MUANGOAI_HOANTHANH_2016'
			END
				
			ELSE
				BEGIN
					SET @soLuongThucChay = 0
					SET @thucChayTruocChietKhau  =0
					SET @thanhTienThucChay =0
					SET @soLuongThayDoi =0
					SET @giaTriThayDoi = 0
					SET @soLuongKhuyenMai = @SoLuong
					SET @thanhTienKhuyenMai =@DonGia*@SoLuong
					SET @soLuongKMThayDoi =0
					SET @giaTriKMThayDoi = 0
					SET @DonViTinh = @donViTinhThucChay
					SET @ghiChu ='MUANGOAI_HOANTHANH_2016'
					
				END
		END
				--PRINT 'HopDongChiTietID : '	 + CONVERT(NVARCHAR(20), @HopDongChiTietID)
				--PRINT @soLuongThucChay
				--PRINT @thucChayTruocChietKhau
				--PRINT @thanhTienThucChay
				--PRINT @soLuongThayDoi
				--PRINT @giaTriThayDoi
				--PRINT @soLuongKhuyenMai
				--PRINT @thanhTienKhuyenMai
				--PRINT @soLuongKMThayDoi
				--PRINT @giaTriKMThayDoi
				IF(@thanhTienThucChay <> 0 OR @giaTriThayDoi <> 0 OR @thanhTienKhuyenMai <> 0 OR @giaTriKMThayDoi <> 0 )
					EXEC dbo.ThucChayDaTinhMuaNgoai_InsertByPhanBoId
					@ngayThucHien,
					@HopDongChiTietID,
					@soLuongThucChay,
					@thucChayTruocChietKhau,
					@thanhTienThucChay,
					@soLuongThayDoi,
					@giaTriThayDoi,
					@soLuongKhuyenMai,
					@thanhTienKhuyenMai,
					@soLuongKMThayDoi,
					@giaTriKMThayDoi,
					@DonViTinh,
					@ghiChu
		
		FETCH NEXT FROM pb_cursor INTO @HopDongChiTietID, @ThanhTien, @SoLuong, @DonGia, @ngayThucHien
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor
    
    SELECT 1
END

```
