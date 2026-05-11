# Stored Procedure: `TinhLaiThucChayMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-22 16:38:54.267000
- **Ngày sửa cuối**: 2017-03-22 16:38:54.267000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE TinhLaiThucChayMobile
	@SoHopDong NVARCHAR(50),
	@NgayThucHien DATETIME
	AS
	BEGIN
		

-------------Tinh lại thuc chay cho phan bo-----------
DELETE FROM ThucChayDaTinhMobile 
		WHERE DmSanPhamREF = 342 AND NgayThucHien = @NgayThucHien AND SoHopDong = @SoHopDong
		AND NOT (DmHinhThucQuangCao = 13 or DmLoaiBannerREF IN (17,18))

EXEC ThucChay_InsertToTemp_Mobile_BySoHopDong @NgayThucHien, @SoHopDong
DECLARE @HopDongChiTietREF1 int
DECLARE vendor_cursor1 CURSOR FOR 
			SELECT distinct A.SoHopDong, A.HopDongChiTietREF			
			FROM ThucChay_MobileTemp A 
			WHERE 1=1 
			and A.NgayThucHien = @NgayThucHien
			AND A.SoHopDong = @SoHopDong
			AND A.HopDongChiTietREF NOT IN (0,1) AND A.HopDongChiTietREF IS NOT NULL
			ORDER BY A.HopDongChiTietREF			

		OPEN vendor_cursor1
		
		FETCH NEXT FROM vendor_cursor1 INTO @SoHopDong,@HopDongChiTietREF1

		WHILE @@FETCH_STATUS = 0
		BEGIN
			SELECT @SoHopDong,@HopDongChiTietREF1
			--Tinh thuc chay rieng cho phan bo
		    IF dbo.ThucChay_IsHopDongChiTietSingle(@HopDongChiTietREF1) = 1				
				EXEC ThucChay_ExcInsertThucChayDaTinhMobileSingle @HopDongChiTietREF1, @NgayThucHien
			--Tinh cho truong hop multi	
		    ELSE IF  (dbo.ThucChay_IsHopDongChiTietSingle(@HopDongChiTietREF1) = 0 AND 
						(SELECT COUNT(ThucChayDaTinhID) FROM ThucChayDaTinhMobile  
						 WHERE HopDongChiTietREF = @HopDongChiTietREF1
						 AND NgayThucHien = @NgayThucHien) = 0)
				
			EXEC [ThucChay_ExcInsertThucChayDaTinhMobileBanner] @NgayThucHien, @SoHopDong, @HopDongChiTietREF1
				
		    ELSE IF dbo.ThucChay_IsHopDongChiTietSingle(@HopDongChiTietREF1) = -1
				BEGIN 
					SELECT 'NOK'										
				end
			FETCH NEXT FROM vendor_cursor1 INTO @SoHopDong,@HopDongChiTietREF1
		END 
		CLOSE vendor_cursor1;
		DEALLOCATE vendor_cursor1;

END

```
