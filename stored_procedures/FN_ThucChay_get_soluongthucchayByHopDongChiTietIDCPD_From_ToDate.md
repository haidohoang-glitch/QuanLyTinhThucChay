# Function: `ThucChay_get_soluongthucchayByHopDongChiTietID CPD_From_ToDate`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2018-05-31 07:51:13.857000
- **Ngày sửa cuối**: 2018-05-31 08:05:20.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
					  
CREATE FUNCTION [dbo].[ThucChay_get_soluongthucchayByHopDongChiTietID CPD_From_ToDate] 
(
		@HopDongChiTietID INT,
        @DmSanPhamREF INT,
        @DonViTinhREF INT,
        @NgayThucHien DATETIME,
        @FromDate DATETIME,
        @ToDate DATETIME)
RETURNS BIGINT
BEGIN
	DECLARE @v_SoLuongThucChay INT,@v_SLTC_NgayBatDau INT, @v_SLTC_NgayKetThuc INT
			, @v_SLHDCT INT, @v_countbanner INT, @HopDongID INT, @v_loaiBanner INT, @ChietKhau INT; 
	DECLARE @v_PhanBoChinhID INT, @v_SoLuongPhanBo INT, @v_isphanbochinh int;
    DECLARE @v_bannerID nvarchar(200), @v_LoaiNenTang INT, @NgayGioiHanTinh DATETIME, @v_ngaythuchiencheck DATETIME
    
    set @v_PhanBoChinhID = 0;
    set @v_isphanbochinh = 0;
    set @HopDongID = 0;
    set @v_countbanner = 0;
    set @v_bannerID = '';
    set @v_SoLuongThucChay = 0;
    set @v_SoLuongPhanBo = 0;
    set @v_PhanBoChinhID  =0;
    set @v_loaiBanner  = 0;
	SET @v_LoaiNenTang = 0
	SET @NgayGioiHanTinh = '2013-01-01'
	/*	XAC DINH CHAY RETAGING	*/
	
	SELECT @v_LoaiNenTang =hdct.DmLoaiNenTangREF, @v_loaiBanner = hdct.DmLoaiBannerREF
	FROM dbo.HopDongChiTiet hdct
	WHERE hdct.DeletedStatus = 0
	AND hdct.HopDongChiTietID = @HopDongChiTietID
	AND NOT((hdct.DmLoaiBannerREF IN (18)) OR (hdct.DmLoaiREF = 13))-- --Khong tinh thuc chay cho HTQC Mua Ngoai
	
	SET @v_LoaiNenTang = ISNULL(@v_LoaiNenTang,0)
	SET @v_loaiBanner = ISNULL(@v_loaiBanner,0)
	 
    /*
    (	-- NHOM SP CPD
	    --140 --Banner CPD
        --,228 -- Boxapp CPD
        --,564 --Boxapp MultiBand
        --,549 --CPD Chuyen trang
    	
    ) 
    */

	IF( (@DmSanPhamREF IN (140,228,564,549,549)) AND (@v_loaiBanner <> 17)) --KHONG PHAI LA CHI PHI SAN PHAM CHINH
	BEGIN
		IF(@v_loaiBanner = 5)
        BEGIN
            IF(@FromDate = '1900-01-01' AND @ToDate = '1900-01-01')
				SET @v_SoLuongThucChay =
				(
                	SELECT SUM(ISNULL((DATEDIFF(DAY,A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1),0)) FROM
					(
						SELECT DISTINCT pb.HopDongFK, pb.HopDongChiTietID, tc.ThoiGianBatDau
						, (CASE WHEN tc.ThoiGianKetThuc > @NgayThucHien THEN @NgayThucHien
							ELSE tc.ThoiGianKetThuc
							END
						)AS ThoiGianKetThuc
						FROM dbo.HopDongChiTiet pb
						INNER JOIN dbo.DotChayHopDongChiTiet tc ON pb.HopDongChiTietID = tc.HopDongChiTietREF
						WHERE 1=1
						AND pb.DmSanPhamREF = @DmSanPhamREF
						AND pb.HopDongChiTietID = @HopDongChiTietID
						AND tc.ThoiGianBatDau <= @NgayThucHien
						AND pb.DeletedStatus = 0
						AND tc.DeletedStatus = 0
					)A
				)
            ELSE
			BEGIN

				IF(@NgayThucHien<@ToDate)
					SET @v_ngaythuchiencheck = @NgayThucHien
				ELSE 
					SET @v_ngaythuchiencheck = @ToDate
			    SET @v_SoLuongThucChay =
				(
                    SELECT SUM(ISNULL((DATEDIFF(DAY, A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1),0)) FROM
					(
						SELECT DISTINCT pb.HopDongFK, pb.HopDongChiTietID
						, ( CASE WHEN tc.ThoiGianBatDau < @FromDate THEN @FromDate
							ELSE tc.ThoiGianBatDau
							END
						)ThoiGianBatDau
						, (CASE WHEN tc.ThoiGianKetThuc > @v_ngaythuchiencheck THEN @v_ngaythuchiencheck
							ELSE tc.ThoiGianKetThuc
							END
						)AS ThoiGianKetThuc
						FROM dbo.HopDongChiTiet pb
						INNER JOIN dbo.DotChayHopDongChiTiet tc ON pb.HopDongChiTietID = tc.HopDongChiTietREF
						WHERE 1=1
						AND pb.DmSanPhamREF = @DmSanPhamREF
						AND pb.HopDongChiTietID = @HopDongChiTietID
						AND NOT(tc.ThoiGianBatDau > @ToDate OR tc.ThoiGianKetThuc <@FromDate)
						AND pb.DeletedStatus = 0
						AND tc.DeletedStatus = 0
				)A  
			)
			END
        END  
    END
	ELSE
    BEGIN
               	IF(@FromDate = '1900-01-01' AND @ToDate = '1900-01-01') 
				BEGIN
					SET @v_SoLuongThucChay =
					(
							SELECT SUM(ISNULL((DATEDIFF(DAY,A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1),0)) FROM
							(
								SELECT DISTINCT pb.HopDongFK, pb.HopDongChiTietID, tc.ThoiGianBatDau, tc.BookingREF
								, (CASE WHEN tc.ThoiGianKetThuc > @NgayThucHien THEN @NgayThucHien
									ELSE tc.ThoiGianKetThuc
									END
								)AS ThoiGianKetThuc
								FROM dbo.HopDongChiTiet pb
								INNER JOIN dbo.DotChayHopDongChiTiet tc ON pb.HopDongChiTietID = tc.HopDongChiTietREF
								WHERE 1=1
								AND pb.DmSanPhamREF = @DmSanPhamREF
								AND pb.HopDongChiTietID = @HopDongChiTietID
								AND tc.ThoiGianBatDau <= @NgayThucHien
								AND tc.DeletedStatus = 0
								AND pb.DeletedStatus = 0
							)A
					) 
				END
                ELSE
				BEGIN
					IF(@NgayThucHien<@ToDate)
						SET @v_ngaythuchiencheck = @NgayThucHien
					ELSE 
						SET @v_ngaythuchiencheck = @ToDate
					SET @v_SoLuongThucChay = 
					(
						SELECT SUM(ISNULL((DATEDIFF(DAY, A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1),0)) FROM
						(
							SELECT DISTINCT pb.HopDongFK, pb.HopDongChiTietID
							, ( CASE WHEN tc.ThoiGianBatDau < @FromDate THEN @FromDate
								ELSE tc.ThoiGianBatDau
								END
							)ThoiGianBatDau
							, tc.BookingREF
							, (CASE WHEN tc.ThoiGianKetThuc > @v_ngaythuchiencheck THEN @v_ngaythuchiencheck
								ELSE tc.ThoiGianKetThuc
								END
							)AS ThoiGianKetThuc
							FROM dbo.HopDongChiTiet pb
							INNER JOIN dbo.DotChayHopDongChiTiet tc ON pb.HopDongChiTietID = tc.HopDongChiTietREF
							WHERE 1=1
							AND pb.DmSanPhamREF = @DmSanPhamREF
							AND pb.HopDongChiTietID = @HopDongChiTietID
							AND NOT(tc.ThoiGianBatDau > @ToDate OR tc.ThoiGianKetThuc <@FromDate)
							AND tc.DeletedStatus = 0
							AND pb.DeletedStatus = 0
						)A  
					)
				END
        END

	 SET @v_SoLuongThucChay = ISNULL(@v_SoLuongThucChay,0)
	RETURN @v_SoLuongThucChay
END
```
